# PPDS 08
Ninth assignment from the PPDS course.

# Implementation
In this assignment, I made 2 simple methods using Cuda to edit images. First, I make an array out of the image using image.imread,
this will give me RGB for each pixel of the image. In the yellow_filter function, I just multiply the blue parameter of the RGB with 0.5 for each pixel
which makes the image yellow. In the gamma function I divide each parameter from RGB for each pixel of the image with 0.6 and this causes the brightness of the image to increase.

