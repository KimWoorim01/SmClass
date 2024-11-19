
# a = 1
# b = 4

# a_tuple = (a,b)
# print(type(a_tuple))

# b_tuple = (a,)
# print(type(b_tuple))

import oracledb

def connections():

  try:
    conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
  except Exception as e: print("error : ",e)
  return conn

num1 = int(input("최소 월급 입력 >> "))
num2 = int(input("최고 월급 입력 >> "))


conn = connections()
cursor = conn.cursor()

sql = f"select * from employees where salary >= {num1} and salary <= {num2}"

cursor.execute(sql)

rows = cursor.fetchall()

for idx,row in enumerate(rows):
  print(row)

conn.close()