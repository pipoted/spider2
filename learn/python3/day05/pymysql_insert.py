# encoding:utf-8

import pymysql


conn = pymysql.connect(
    host='localhost',
    user='root',
    password='xzx199110',
    database='spider',
    port=3306,
)

# cursor = conn.cursor()
# sql = """
# insert into user(id, username, age, password) values(2, 'xiaojian', 20, 199110)
# """
# cursor.execute(sql)
# conn.commit()

username = 'xiaojianjian'
age = 21
password = '199110'

cursor = conn.cursor()
sql = """
insert into user(id, username, age, password) values(null, %s, %s, %s)
"""
cursor.execute(sql, (username, age, password))
conn.commit()

conn.close()
