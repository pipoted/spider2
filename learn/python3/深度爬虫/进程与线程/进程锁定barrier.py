# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-04 16:23'

import multiprocessing
import os


def get_data(data):
    with my_barrier:
        print(os.getpid(), 'start')
        # time.sleep(3)
        print(os.getpid(), 'end', data * data)


if __name__ == '__main__':
    my_barrier = multiprocessing.Barrier(3)
    my_list = [x for x in range(100)]

    process_list = []
    for data in my_list:
        process = multiprocessing.Process(target=get_data, args=(data,))
        process_list.append(process)
        process.start()

    for process in process_list:
        process.join()
