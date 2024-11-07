import oracledb

def connections():

  try:
    conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
  except Exception as e: print("error : ",e)
  return conn


conn = connections()
cursor = conn.cursor()

name = input("이름 검색 >> ")

sql = f"select * from employees where emp_name like '%{name}%'"

# execute 뒤에는 dict, list, tuple 만 가능함.
cursor.execute(sql)

rows = cursor.fetchall()

for idx,row in enumerate(rows):
  print(f"{idx}. 번호:{row[0]}\t 이름:{row[1]}\t 국어:{row[2]}\t 영어:{row[3]}\t 수학:{row[4]}\t 합계:{row[5]}\t 평균:{row[6]}")


conn.close()

