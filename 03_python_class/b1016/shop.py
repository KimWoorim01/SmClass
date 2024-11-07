
member = [
  {"id":"aaa","pw":"1111","name":"홍길동","nicName":"길동스","address":"서울시", "money": 1000000},
  {"id":"bbb","pw":"2222","name":"이순신","nicName":"치트공","address":"부산시", "money": 1000000},
  {"id":"ccc","pw":"3333","name":"유관순","nicName":"3.1운동","address":"경기도", "money": 1000000},
  {"id":"ddd","pw":"4444","name":"강감찬","nicName":"거란컷","address":"인천시", "money": 1000000},
  {"id":"eee","pw":"5555","name":"김구","nicName":"독립운동가","address":"대구시", "money": 1000000}
]

product = [
  {"pno":1,"product_code":"s_001","product_name":"삼성TV","price":5000000,"color":"black"},
  {"pno":2,"product_code":"l_011","product_name":"LG냉장고","price":2000000,"color":"red"},
  {"pno":3,"product_code":"h_003","product_name":"하만카돈스피커","price":500000,"color":"black"},
  {"pno":4,"product_code":"a_005","product_name":"세탁기","price":1000000,"color":"white"},

]
cart = []

session_info = {}
money = 0
cart_no = 0

p_title = [
  "상품코드", "상품명", "가격"
]

def choice_data(code ,product, session_info):

  for pro in product :
    if pro["product_code"] == code :
      print(f"{pro["product_name"]} 를 구매하셨습니다.")
      print("구매내역에 등록합니다.")

      data = {"cno":cart_no, "id":session_info["id"], "name":session_info["name"], "pCode":pro["product_code"], "pName":pro["product_name"],"price":pro["price"]}
      
      return data
  
  print("데이터 입력 오류, 상품을 찾을수 없습니다.")
  return

while True:
  input_id = input("아이디 입력 >> ")
  input_pw = input("비밀번호 입력 >> ")

  flag = 0

  for mem in member :
    if mem["id"] == input_id and mem["pw"] == input_pw:
      session_info = mem
      print("로그인 성공")
      flag = 1
      break

  if flag == 0:
    print("로그인 실패 아이디&비밀번호 재입력 요망")
  else :
    break


while True:

  print("[ SM-SHOP 프로그램 ]")

  print(f"                    {session_info["nicName"]} 님")
  print(f"충전금액             {session_info["money"]}")

  print("")
  product_count = 1
  for data in product:
    print(f"{product_count}. {data["product_name"]} - {data["price"]}")
    product_count += 1

  print("8. 구매내역")
  print("9. 금액충전")

  choice = input("구매하려는 상품 번호 입력 >> ")
  

  if choice == "1" :
    cart_no += 1
    data = choice_data("s_001", product, session_info)
    cart.append(data)
  elif choice == "2":
    cart_no += 1
    data = choice_data("l_011", product, session_info)
    cart.append(data)
  elif choice == "3":
    cart_no += 1
    data = choice_data("h_003", product, session_info)
    cart.append(data)
  elif choice == "4":
    cart_no += 1
    data = choice_data("a_005", product, session_info)
    cart.append(data)

  elif choice == "8":

    print(f"구매할 상품의 갯수 : {cart_no}")

    total_price = 0
    if cart != "" :
      print(f"{p_title[0]}\t{p_title[1]}\t{p_title[2]}\t{p_title[3]}")

      for i in cart:
        print(f"{i["pCode"]}\t{i["pName"]}\t{i["price"]}")
        total_price += i["price"]
        print()
    
    print(f"총 결제 금액 : {total_price}")


  elif choice == "9":

    input_price = int(input("충전할 금액 >> "))
    session_info["money"] += input_price

    for mem in member :
      if mem["id"] == session_info["id"] and mem["pw"] == session_info["pw"]:
        mem["money"] = session_info["money"]
  

