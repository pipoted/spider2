# encoding='utf-8'

import csv


def read_csv_demo1():
    with open('test.csv', 'r') as fp:
        # reader 是迭代器
        reader = csv.reader(fp)
        titles = next(reader)
        for x in reader:
            print(x)


def read_csv_demo2():
    with open('test.csv', 'r') as fp:
        # 使用dictreader创建的reader对象， 不会包含标题那行数据
        reader = csv.DictReader(fp)
        for x in reader:
            print(x)


if __name__ == '__main__':
    read_csv_demo2()
