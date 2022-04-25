# PPDS 08
Ninth assignment from the PPDS course.

# Implementation
In this assignment, I made 2 simple methods using Cuda to edit images. First, I make an array out of the image using image.imread,
this will give me RGB for each pixel of the image. In the yellow_filter function, I just multiply the blue parameter of the RGB with 0.5 for each pixel
which makes the image yellow. In the gamma function I divide each parameter from RGB for each pixel of the image with 0.6 and this causes the brightness of the image to increase.

In the images below you can see the original image on the left and on the right you can see the image after editing with the yellow_filter function.
<p align="left">
    <img src="https://raw.githubusercontent.com/Sajmooooon/ppds/09/bg.png?token=GHSAT0AAAAAABSB25NJ2H3O2JAJ76KSFUKYYTGS2IQ" height="213" width="320"/>
    <img src="https://raw.githubusercontent.com/Sajmooooon/ppds/09/bg_out.png?token=GHSAT0AAAAAABSB25NJI6JEYLQ4BJSJQ3ZUYTGS2QA" height="213" width="320"/>
</p>

In the images below you can see the original image on the left and on the right you can see the image after editing with the gamma function.
<p align="left">
    <img src="https://raw.githubusercontent.com/Sajmooooon/ppds/09/shrek.png?token=GHSAT0AAAAAABSB25NINFAHPBSJYNUMN5XQYTGS3ZA" height="250" width="235"/>
    <img src="https://raw.githubusercontent.com/Sajmooooon/ppds/09/shrek_out.png?token=GHSAT0AAAAAABSB25NIHWMTJ5MMG5G2UZVKYTGS4BQ" height="250" width="235"/>
</p>

