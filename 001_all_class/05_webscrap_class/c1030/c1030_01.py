import oracledb
import smtplib

def connections():

  try:
    conn = oracledb.connect(user='ora_user',password='1111',dsn='localhost:1521/xe')
  except Exception as e: print("error : ",e)
  return conn


conn = connections()
cursor = conn.cursor()

print("[커뮤니티]")
print("1. 로그인")
print("2. 비밀번호 찾기")
print("3. 회원가입")
print("*"*70)


choice = input("원하는 항목 선택 >> ")

if choice == "1":
  print("[로그인]")
  print("0. 메뉴로 나가기")
  while True:

    
    user_id = input("아이디를 입력하세요 >> ")

    if user_id == "0":
      break

    user_pw = input("비밀번호를 입력하세요 >> ")

    User_ID_Check_sql = f"select * from member where id = '{user_id}'"
    User_PW_Check_sql = f"select * from member where id = '{user_id}' and pw = '{user_pw}'"
    
    cursor.execute(User_ID_Check_sql)
    rows = cursor.fetchall()

    if len(rows) <= 0:
      print("존재하지 않는 아이디 입니다.")
      continue
      
    cursor.execute(User_PW_Check_sql)
    rows = cursor.fetchall()

    if len(rows) <= 0:
      print("비밀번호가 일치하지 않습니다.")
      continue

    print("로그인 성공")
    break

  pass
elif choice == "2":

  print("[비밀번호 찾기]")
  print("0. 메뉴로 나가기")
  while True:
      
    user_id = input("아이디를 입력하세요 >> ")

    if user_id == "0":
      break

    User_ID_Check_sql = f"select * from member where id = '{user_id}'"
    
    cursor.execute(User_ID_Check_sql)
    rows = cursor.fetchall()

    if len(rows) <= 0:
      print("존재하지 않는 아이디 입니다.")
      continue
    
    user_pw = input("임시 비밀번호를 입력해주세요. >> ")

    user_update_sql = f"update member set pw = {user_pw} where id = {user_id}"
    cursor.execute(user_update_sql)
    
    
    conn.commit()

    break


  pass
elif choice == "3":
  pass


conn.close()