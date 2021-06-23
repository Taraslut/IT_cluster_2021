import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    port=3306,
    cursorclass=pymysql.cursors.DictCursor
)

cursor = conn.cursor()

cursor.execute('show databases')

for item in cursor.fetchall():
    print(item)
