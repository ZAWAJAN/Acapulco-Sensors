#!/bin/bash
#v03 09-01-25

## set the path variable, particularly useful if you're using cron to schedule captures
export PATH=$PATH:/usr/local/bin/:/usr/local/lib/ray:/home/acapulco/PiHDR:/home/acapulco/PiHDR/man1

# move to the directory
cd /home/acapulco/PiHDR
 
# create a directory with date and time. The $dir variable is also used for filenames
dir=`date +"%Y%m%d_%H%M"`
mkdir $dir

cd $dir

# Call the lux reading Python script providing the timestamp (dir)...
# as the file name to save the reading
python3 /home/acapulco/PiHDR/lux_sensor.py $dir

# call the python script to control the camera
python3 /home/acapulco/PiHDR/exposurebracket.py

exiftool -overwrite_original -ISO=100 *.jpg 
exiftool -overwrite_original -ISO -ApertureValue>FNumber *.jpg 
exiftool -overwrite_original -FNumber=2.6 *.jpg 

# create the .rsp file and the HDR image (get hdrgen from anyhere.com). If a tested response function file already exists, change the ".rsp" file name in the `hdrgen` command to match the existing one.
# hdrgen ./ldr_??.jpg -o ${dir}.hdr -r existing_response_function.rsp -a -e -f -g
hdrgen ./ldr_??.jpg -o ${dir}.hdr -r response_function_${dir}.rsp -a -e -f -g

## HDR image calibration

# Nullification of exposure value
ra_xyze -r -o ${dir}.hdr > ${dir}_01_EVinpixel.hdr

# cropping the HDR image
pcompos -h -x 2711 -y 2711 ${dir}_01_EVinpixel.hdr -714 -106 > ${dir}_02_cropped.hdr

# resize the HDR image
pfilt -1 -x 1500 -y 1500 ${dir}_02_cropped.hdr > ${dir}_03_resized.hdr

# projection adjustment (using the default equisolid to equidistant function)
pcomb -h -f fisheye_corr.cal -e 'rad(r)=mapsolid(r)' ${dir}_03_resized.hdr > ${dir}_04_equidistantproj.hdr

# vignetting correction
pcomb -f ../VignettingCorrection.cal ${dir}_04_equidistantproj.hdr > ${dir}_05_vignettingcorrected.hdr

# adjust exposure and add view information
pfilt -1 ${dir}_05_vignettingcorrected.hdr | getinfo -a "VIEW= -vta -vh 184 -vv 184" > ${dir}_final.hdr

# calculate illuminance from luminance map
evalglare -V ${dir}_final.hdr > Ev.txt &

# create a falsecolor image & convert to tif
falsecolor -s 200000 -log 5 -ip ${dir}_final.hdr | ra_tiff -z - ${dir}_falsecolor.tif &

# create a tone mapped luminance photo
pcond ${dir}_final.hdr | ra_tiff -z - ${dir}.tif &

# create a JPG of the tiff for use as well 
# note: this requires the installition of imageMagick
# wait for the three background analysis processes above to complete. 
wait
convert	${dir}.tif ${dir}.jpg
wait



 
