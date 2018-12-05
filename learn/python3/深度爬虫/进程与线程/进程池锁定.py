# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-04 16:01'

import multiprocessing
import os


def get_data(data):
    print(os.getpid(), 'start')
    # time.sleep(3)
    print(os.getpid(), 'end')
    return data * data


if __name__ == '__main__':
    my_list = [x for x in range(100)]
    pool = multiprocessing.Pool(processes=4)
    pool_output = pool.map(get_data, my_list)
    pool.close()
    pool.join()
    print(pool_output)
