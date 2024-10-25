


sub = ["id","pw","name","nickname","address","money"]
member = []

def search_id(checkId):
  for data in member :
    if data["id"].find(checkId) != -1 :
      count += 1
      return True
  return False

while True:

  print("1.회원등록")
  print("2.회원검색")
  print("7.회원파일 읽어서 저장")

  choice = input("항목 선택 >> ")

  if choice == "1":
    while True:
      id = input("ID 입력 >> ")
      if search_id(id) == True:
        continue
      else:
        print(f"{id}는 사용 가능합니다.")

      if id == "end" :
        break
      
      pw = input("PW 입력 >> ")
      name = input("이름 입력 >> ")
      nick = input("닉네임 입력 >> ")
      address = input("주소 입력")
      money = int(input("충전 금액 입력 >> "))

      m_list = [id,pw,name,nick,address,money]
      member.append(dict(zip(sub,m_list)))

  elif choice == "2":
    count = 0
    checkId = input("아이디 검색")
    for data in member :
      if data["id"].find(checkId) != -1 :
        print(data["id"],end=",\t")
        count += 1
        continue
    print()

    if count == 0 :
      print("검색결과 없음")
    else:
      print(f"{count}개 찾았습니다.")
  elif choice == "7":
    f = open("b1017/member.txt","r",encoding="utf-8")
    while True:
      line = f.readline()
      if not line:break
      lineCount += 1
      s = line.strip().split(",")
      s[5] = int(s[5])
      member.append(dict(zip(sub,s)))
    f.close
        
        
# lineCount = 0
# while True:
#   line = f.readline()
#   if not line:break
#   lineCount += 1
#   s = line.strip().split(",")
#   s[5] = int(s[5])
#   member.append(dict(zip(sub,s)))

# print(len(member))
# count = 0
# checkId = input("아이디 검색")
# for data in member :
#   if data["id"].find(checkId) != -1 :
#     print(data["id"],end=",\t")
#     count += 1
#     continue
# print()

# if count == 0 :
#   print("검색결과 없음")
# else:
#   print(f"{count}개 찾았습니다.")





