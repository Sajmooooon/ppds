"""
Authors: Bc. Simon Youssef
         Mgr. Ing. Matúš Jókay, PhD.
Coppyright 2022 All Rights Reserved.
Resources:
https://www.delftstack.com/es/howto/python/convert-image-to-grayscale-python/
https://www.scratchapixel.com/lessons/digital-imaging/simple-image-manipulations/image-processing
Implementation of adding yellow filter and brightness to images with streams.
"""

from matplotlib import image
from matplotlib import pyplot
from numba import cuda
from time import perf_counter
import numpy as np
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


def show_image(image_arr):
    """
    Function for showing image.

    Parameter:
        image_arr: Array of image.
    """

    pyplot.figure()
    figure = pyplot.gcf()
    figure.subplots_adjust(bottom=0, top=1, left=0, right=1)

    for i in range(len(image_arr)):
        figure.tight_layout()
        sub = figure.add_subplot(8, 1, i + 1)
        pyplot.axis('off')
        pyplot.imshow(image_arr[i], interpolation='nearest')

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


def init(arr_len, file_name, type):
    """
    Function to get blocks per grid.

    Parameter:
        arr_len: Length of array.
        file_name: Name of file.
        type: Type of function to use (0 - yellow_filter, else - gamma).
    """

    data_gpu = []
    gpu_out = []
    streams = []

    start_events = []
    end_events = []

    threadsperblock = (32, 32)

    image1 = image.imread(file_name)
    num = math.ceil(len(image1)/arr_len)
    last = 0

    for _ in range(arr_len):
        streams.append(cuda.stream())
        start_events.append(cuda.event(timing=True))
        end_events.append(cuda.event(timing=True))

    t_start = perf_counter()

    for i in range(arr_len):
        before = last
        last += num

        if i == arr_len-1:
            data_gpu.append(cuda.to_device(image1[before: len(image1)-1],
                                           stream=streams[i]))
        else:
            data_gpu.append(cuda.to_device(image1[before: last],
                                           stream=streams[i]))

    for j in range(arr_len):
        blockspergrid = get_blockspergrid(data_gpu[j], threadsperblock)
        start_events[j].record(streams[j])
        if type:
            gamma[blockspergrid, threadsperblock, streams[j]](data_gpu[j])
        else:
            yellow_filter[blockspergrid, threadsperblock, streams[j]](data_gpu[j])

    for i in range(arr_len):
        end_events[i].record(streams[i])
        gpu_out.append(data_gpu[i].copy_to_host(stream=streams[i]))

    t_end = perf_counter()

    kernel_times = []

    for k in range(arr_len):
        kernel_times.append(
            cuda.event_elapsed_time(start_events[k], end_events[k]))

    print(f'Total time: {t_end - t_start:.2f} s')
    print(f'Mean kernel duration (milliseconds): '
          f'{ np.mean(kernel_times):.2f} ')
    print(f'Mean kernel standard deviation (milliseconds): '
          f'{ np.std(kernel_times):.2f}')

    show_image(gpu_out)


init(4, "bg.png", 1)
init(4, "bg.png", 0)
