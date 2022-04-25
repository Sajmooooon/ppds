"""
Authors: Bc. Simon Youssef
         Mgr. Ing. Matúš Jókay, PhD.
Coppyright 2022 All Rights Reserved.
Resources:
https://www.delftstack.com/es/howto/python/convert-image-to-grayscale-python/
https://www.scratchapixel.com/lessons/digital-imaging/simple-image-manipulations/image-processing
Implementation of adding yellow filter and brightness to images with cuda.
"""


from matplotlib import image
from matplotlib import pyplot
from numba import cuda
import math


@cuda.jit
def yellow_filter(io_array):
    """
    Simple function to add yellow filter to image.

    Parameter:
        io_array: Array of image.
    """

    x, y = cuda.grid(2)
    x_max = io_array.shape[0]
    y_max = io_array.shape[1]

    if x < x_max and y < y_max:
        io_array[x][y][2] *= 0.5


@cuda.jit
def gamma(io_array):
    """
    Simple function to increase brightness of image.

    Parameter:
        io_array: Array of image.
    """

    x, y = cuda.grid(2)
    x_max = io_array.shape[0]
    y_max = io_array.shape[1]

    if x < x_max and y < y_max:
        io_array[x][y][0] /= 0.6
        io_array[x][y][1] /= 0.6
        io_array[x][y][2] /= 0.6


def get_image(image_arr, file_name):
    """
    Function for showing image and saving it to file.

    Parameter:
        image_arr: Array of image.
        file_name: Name of file.
    """

    figure = pyplot.gcf()
    figure.subplots_adjust(bottom=0, top=1, left=0, right=1)
    pyplot.imshow(image_arr)
    pyplot.axis('off')
    pyplot.savefig(file_name, bbox_inches='tight', pad_inches=0)
    pyplot.show()
    pyplot.close()


def get_blockspergrid(image_arr, threadsperblock):
    """
    Function to get blocks per grid.

    Parameter:
        image_arr: Array of image.
        threadsperblock: Tuple of threads per block.
    """

    blockspergrid_x = math.ceil(image_arr.shape[0] / threadsperblock[0])
    blockspergrid_y = math.ceil(image_arr.shape[1] / threadsperblock[1])
    blockspergrid = (blockspergrid_x, blockspergrid_y)
    return blockspergrid


threadsperblock = (32, 32)

image1 = image.imread("bg.png")
blockspergrid = get_blockspergrid(image1, threadsperblock)
yellow_filter[blockspergrid, threadsperblock](image1)
get_image(image1, "bg_out.png")

image2 = image.imread("shrek.png")
blockspergrid = get_blockspergrid(image2, threadsperblock)
gamma[blockspergrid, threadsperblock](image2)
get_image(image2, "shrek_out.png")
