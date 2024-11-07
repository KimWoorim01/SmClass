import oracledb

def connections():

  try:
    conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
  except Exception as e: print("error : ",e)
  return conn


conn = connections()
cursor = conn.cursor()

title = [
  "no",
  "name",
  "salary"
]


sql = "select employee_id, emp_name, salary from employees"

cursor.execute(sql)
data = cursor.fetchall()


a_list = []

for i in data:
  a_list.append(dict(zip(title,i)))

print(a_list)


conn.close()