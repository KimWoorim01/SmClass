import oracledb

conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")

print(conn.version)

cursor = conn.cursor()

sql = "select * from member"

cursor.execute(sql)

rows = cursor.fetchall()

print(rows[0][0], rows[0][1], rows[0][2])




conn.close()

input("엔터 입력")