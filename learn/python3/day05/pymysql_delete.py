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
# delete from user where id = 1
# """
# cursor.execute(sql)
# conn.commit()
# conn.close()


cursor = conn.cursor()
sql = """
update user set username = 'hello' where id = 2
"""
cursor.execute(sql)
conn.commit()
conn.close()
