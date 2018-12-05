# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-04 16:01'

import threading
import time


def my_thread(name):
    with sep:
        for i in range(10):
            time.sleep(1)
            print(name, str(i), threading.currentThread().name)


sep = threading.Semaphore(3)
thread_list = []
for name in ['a', 'b', 'c', 'd', 'e']:
    my_thd = threading.Thread(target=my_thread, args=(name,))
    my_thd.start()
    thread_list.append(my_thd)

for thread in thread_list:
    thread.join()
