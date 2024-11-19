import oracledb
## sql developer 실행
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
## sql창이 열림
cursor = conn.cursor()
# sql작성,실행
sql = "select * from students"
cursor.execute(sql)

rows = cursor.fetchall()

for idx,row in enumerate(rows):
  print(f"{idx}. 번호:{row[0]}\t 이름:{row[1]}\t 국어:{row[2]}\t 영어:{row[3]}\t 수학:{row[4]}\t 합계:{row[5]}\t 평균:{row[6]}")


conn.close()