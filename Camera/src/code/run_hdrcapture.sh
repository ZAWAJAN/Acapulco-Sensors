#!/bin/bash
#v02 05-11-24

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

exiftool -ISO=100 *.jpg 
exiftool -ISO -ApertureValue>FNumber *.jpg 
exiftool -FNumber=2.6 *.jpg 

# create the .rsp file and the HDR image (get hdrgen from anyhere.com)
hdrgen ./ldr_01.jpg ./ldr_02.jpg ./ldr_03.jpg ./ldr_04.jpg ./ldr_05.jpg ./ldr_06.jpg ./ldr_07.jpg ./ldr_08.jpg ./ldr_09.jpg ./ldr_10.jpg -o ${dir}.hdr -r response_function_${dir}.rsp -a -e -f -g

## HDR image calibration

# Nullification of exposure value
ra_xyze -r -o ${dir}.hdr > ${dir}_01_EVinpixel.hdr

# cropping the HDR image
pcompos -x 2711 -y 2711 ${dir}_01_EVinpixel.hdr -714 -106 > ${dir}_02_cropped.hdr

# resize the HDR image
pfilt -1 -x 1500 -y 1500 ${dir}_02_cropped.hdr > ${dir}_03_resized.hdr

# projection adjustment (using the default equisolid to equidistant function)
pcomb -f FisheyeCorrection.cal -e 'rad(r)=mapsolid(r)' ${dir}_03_resized.hdr > ${dir}_04_equidistantproj.hdr

# vignetting correction
pcomb -f VignettingCorrection.cal ${dir}_04_equidistantproj.hdr > ${dir}_05_vignettingcorrected.hdr

# make a smaller image for quicker analysis
pfilt -1 -x 1500 -y 1500 ${dir}_05_vignettingcorrected.hdr | getinfo -a "VIEW= -vta -vh 184 -vv 184" > ${dir}.pic
# if you're interested in a full resolution HDR you may want to use the line below
# and comment the line above with a "#", FULL RESOLUTION CAN TAKE SOME TIME TO CREATE
# pfilt -1 -e 1 ${dir}.hdr > ${dir}.pic

# calculate glare metrics
evalglare -vta -vv 184 -vh 184 -V ${dir}.pic > glare.txt &

# create a falsecolor image & convert to tif
falsecolor -s 200000 -log 5 -ip ${dir}.pic | ra_tiff -z - ${dir}_falsecolor.tif &

# create a tone mapped luminance photo
pcond ${dir}.pic | ra_tiff -z - ${dir}.tif &

# create a JPG of the tiff for use as well 
# note: this requires the installition of imageMagick
# wait for the three background analysis processes above to complete. 
wait
convert	${dir}.tif ${dir}.jpg
wait



 
