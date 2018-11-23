# encoding: utf-8

import time
import threading


def coding():
    for x in range(10):
        print(threading.current_thread())
        time.sleep(1)


def draw():
    for x in range(10):
        print('drawing %s' % threading.current_thread())
        time.sleep(1)


def main():
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=draw)

    t1.start()
    t2.start()

    print(threading.enumerate())


if __name__ == '__main__':
    main()
