# coding=utf-8
__author__ = 'xiao'
__date__ = '2018-12-04 15:07'

import multiprocessing  # 分布式进程
import time
import random

from queue import Queue
from multiprocessing import managers  # 分布式进程管理器

task_queue = Queue()  # 任务队列
result_queue = Queue()  # 结果队列


def return_task():
    return task_queue


def return_result():
    return result_queue
