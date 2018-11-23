import threading
import random
import time

G_MONEY = 1000
G_CONDITION = threading.Condition()
G_TOTAL_TIMES = 10
G_TIMES = 0


class Producer(threading.Thread):
    def run(self):
        global G_MONEY
        global G_TIMES
        global G_TOTAL_TIMES

        while True:
            money = random.randint(100, 1000)
            G_CONDITION.acquire()

            if G_TIMES >= G_TOTAL_TIMES:
                G_CONDITION.release()
                break

            G_MONEY += money
            print('Producer:', threading.current_thread(), money, G_MONEY)
            G_TIMES += 1

            G_CONDITION.notify_all()
            G_CONDITION.release()
            time.sleep(0.5)


class Consumer(threading.Thread):
    def run(self):
        global G_MONEY
        while True:
            money = random.randint(100, 1000)
            G_CONDITION.acquire()
            while G_MONEY < money:
                if G_TIMES >= G_TOTAL_TIMES:
                    G_CONDITION.release()
                    return

                G_CONDITION.wait()

            G_MONEY -= money
            print('Consumer:', threading.current_thread, G_MONEY, money)
            G_CONDITION.release()
            time.sleep(0.5)


def main():
    for x in range(5):
        t = Producer(name='Producer %d' % x)
        t.start()

    for x in range(5):
        t = Consumer(name='Consumer %d' % x)
        t.start()


if __name__ == '__main__':
    main()
