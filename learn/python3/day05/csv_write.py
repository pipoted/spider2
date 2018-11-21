# encoding='utf-8'

import csv


def write_csv_demo1():
    headers = ['username', 'age', 'height']
    values = [
        ('张三', 21, 170),
        ('肖见', 21, 178),
    ]

    with open('classroom.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(values)


def write_csv_demo2():
    headers = ['username', 'age', 'height']
    value = [
        {'username': '张三', 'age': 21, 'height': 172},
        {'username': '肖见', 'age': 21, 'height': 172},
    ]
    with open('classroom1.csv', 'w', encoding='utf-8', newline='') as fp:
        writer = csv.DictWriter(fp, headers)
        writer.writeheader()
        writer.writerows(value)


if __name__ == '__main__':
    write_csv_demo2()
