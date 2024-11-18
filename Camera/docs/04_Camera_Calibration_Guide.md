# HDR Camera Calibration Guide

To end up with a standarized and useful HDR image, various adjustments have to be applied after the multiple exposures are taken and the base HDR image is produced with hdrgen.

This whole process is described in the [Tutorial: Luminance Maps for Daylighting Studies from High Dynamic Range Photography](https://infoscience.epfl.ch/bitstreams/5de7b455-0f0b-4cba-be41-0478e5abb181/download) in detail. 
We will not cover it extensively here, so please refer to beforementioned paper.

## Calibration Steps

Adapted from [Clotilde Pierson. Coralie Cauwerts, Magali Bodart, Jan Wienold, 2020](https://www.researchgate.net/publication/338386406_Tutorial_Luminance_Maps_for_Daylighting_Studies_from_High_Dynamic_Range_Photography).

1. Response function
	- This is being done automatically by `hdrgen` while merging the multiple exposures into HDR.
	- Best practice is to get the response function correction file while making an HDR in a daylit room with one window, facing that window, in an overcast day. You later reuse that file providing it to the `hdrgen` command.
2. Cropping and resizing the HDR image
	- This crops the image to square encompassing a circle of your lens fisheye view.
	- You have to know dimentions of your Image and pixel coordinates. This can be done in any image editing software like Gimp, Affinity Photo or Photoshop.
3. Projection Adjustment:
	- You need to figure out the projection of you fisheye camera and apply a specific correction in a .cal file
	- Refer to [A method for estimating fisheye lens’ field-of view angle and projection for HDR luminance capture](https://pure.tudelft.nl/ws/portalfiles/portal/57456665/x046_PO061.pdf) for instructions.
4. Vignetting Correction - Determination of Vignetting Curves:
	- You have to determine the rate at which the HDR image is getting darker towards the edges of the fisheye circular field of view.
	- You can find instructions on page 13 of the paper.
	- Also refer to [this blog post](https://discourse.radiance-online.org/t/help-with-creating-a-vignetting-cal-file/5745), and [this one](https://discourse.radiance-online.org/t/vignetting-correction-calibration-file/5962).
