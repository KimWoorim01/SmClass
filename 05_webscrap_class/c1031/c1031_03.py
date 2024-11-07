# 입력한 달 이상의 입사한 사원을 출력하시오

import oracledb

def connects():
  user = "ora_user"
  password = "1111"
  dsn = "localhost:1521/xe"

  try:
    conn = oracledb.connect(user=user, password=password, dsn= dsn)
  except Exception as e:
    print("error : ",e)
  return conn



conn = connects()
cursor = conn.cursor()


d_day = input("입력한 달 입력 >> ")

sql = f"select * from employees where substr(hire_date,4,2) >= {d_day}"

cursor.execute(sql)

resultData = cursor.fetchall()

for data in resultData:
  print(data)
  print()