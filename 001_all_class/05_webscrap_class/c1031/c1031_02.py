# 오라클 db에서는 타입 결정
# 문자형(숫자만) 타입 + 숫자와 사칙연산 됨.
# 파이썬에서 호출한 타입의 결과값이 어떻게 되는지

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

sql = "select * from chartable"