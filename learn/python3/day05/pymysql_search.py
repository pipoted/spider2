import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='xzx199110',
    database='spider',
    port=3306,
)

cursor = conn.cursor()

sql = """
select username, password from user
"""
cursor.execute(sql)
# result = cursor.fetchone()
# print(result)
# result = cursor.fetchone()
# print(result)

results = cursor.fetchall()
print(results)

conn.close()
