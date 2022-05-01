from matplotlib import image
from matplotlib import pyplot
from numba import cuda
from time import perf_counter
import math


@cuda.jit
def yellow_filter(io_array):
    x, y = cuda.grid(2)
    x_max = io_array.shape[0]
    y_max = io_array.shape[1]

    if x < x_max and y < y_max:
        io_array[x][y][2] *= 0.5


@cuda.jit
def gamma(io_array):
    x, y = cuda.grid(2)
    x_max = io_array.shape[0]
    y_max = io_array.shape[1]

    if x < x_max and y < y_max:
        io_array[x][y][0] /= 0.6
        io_array[x][y][1] /= 0.6
        io_array[x][y][2] /= 0.6


def show_image(image_arr):
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
    blockspergrid_x = math.ceil(image_arr.shape[0] / threadsperblock[0])
    blockspergrid_y = math.ceil(image_arr.shape[1] / threadsperblock[1])
    blockspergrid = (blockspergrid_x, blockspergrid_y)
    return blockspergrid


def init(arr_len, file_name, type):
    data_gpu = []
    gpu_out = []
    streams = []

    threadsperblock = (32, 32)

    image1 = image.imread(file_name)
    num = math.ceil(len(image1)/arr_len)
    last = 0

    for _ in range(arr_len):
        streams.append(cuda.stream())

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
        if type:
            gamma[blockspergrid, threadsperblock, streams[j]](data_gpu[j])
        else:
            yellow_filter[blockspergrid, threadsperblock, streams[j]](data_gpu[j])

    for i in range(arr_len):
        gpu_out.append(data_gpu[i].copy_to_host(stream=streams[i]))

    t_end = perf_counter()
    print(f'Total time: {t_end - t_start:.2f} s')

    show_image(gpu_out)


init(4, "bg.png", 1)
init(4, "bg.png", 0)
