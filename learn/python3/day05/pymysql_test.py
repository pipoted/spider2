# encoding:utf-8

import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='xzx199110',
    database='spider',
    port=3306,
)

cursor = conn.cursor()

cursor.execute('select 1')
result = cursor.fetchone()
print(result)


conn.close()
