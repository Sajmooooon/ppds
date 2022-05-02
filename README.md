# PPDS 10
Tenth assignment from the PPDS course.

# Implementation
In this assignment, I did an edit of assignment 9 to use multiple streams. At the beginning I used imread to get the array from the picture.
I then split this array into 4 almost equally long parts and loaded them into the data_gpu array, while generating one stream for each part.
Then, just like in the previous assignment, I calculated blocks per grid, with the only change that I calculated it for each part of the array and then ran the individual functions (yellow_filter and gamma).
I then appended the results to the gpu_out array and displayed the image for each part using imshow.
This allowed me to achieve asynchronous execution and thus the image was edited faster.

# Measurements
With yellow_filter function without streams, the image was edited
0.32 seconds and around 0.20 - 0.21 seconds after using streams. For the gamma function without streams, the image was adjusted for 0.58 seconds and after adding streams around 0.19 - 0.21 seconds.
I performed the tests on the bg.png image.

Measurements for gamma function:

<img src="https://i.imgur.com/m9d6ZLg.png"/>


Measurements for yellow_filter function:

<img src="https://i.imgur.com/e3hWywC.png"/>



