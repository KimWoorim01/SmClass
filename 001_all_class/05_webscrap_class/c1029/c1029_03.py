import oracledb
## sql developer 실행
conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
cursor = conn.cursor()


kor = int(input("국어점수 입력 >> "))
eng = int(input("영어점수 입력 >> "))
math = int(input("수학점수 입력 >> "))


sql = f"select * from students where kor > {kor} and eng > {eng} and math > {math}"
cursor.execute(sql)

rows = cursor.fetchall()

for idx,row in enumerate(rows):
  print(f"{idx}. 번호:{row[0]}\t 이름:{row[1]}\t 국어:{row[2]}\t 영어:{row[3]}\t 수학:{row[4]}\t 합계:{row[5]}\t 평균:{row[6]}")


conn.close()