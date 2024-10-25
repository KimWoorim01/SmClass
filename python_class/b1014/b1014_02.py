

def operate(choice , count):
  if count == 0 :
    print("횟수 입력 다시")
    return

  if choice == 1 :
    for i in range(count):
      print("한국어 인사 : 안녕하세요")
      print("영어 인사 : Hello")
      
  elif choice == 2: 
    for i in range(count):
      print("한국어 인사 : 안녕하세요")
      print("일본어 인사 : 오하요(ohayo)")

  elif choice == 3: 
    for i in range(count):
      print("한국어 인사 : 안녕하세요")
      print("중국어 인사 : 니하오(Ni hao)")

  elif choice == 4: 
    for i in range(count):
      print("한국어 인사 : 안녕하세요")
      print("프랑스 인사 : 봉주르(Bonjour)")

  elif choice == 5:
    return
  pass


while True:
  print("[ 외국어 인사 ]")
  print("1. 영어 인사")
  print("2. 일본어 인사")
  print("3. 중국어 인사")
  print("4. 프랑스 인사")

  choice = int(input("원하는 번호 입력 >> "))
  count = int(input("반복횟수 >> "))

  operate(choice, count)
  
  if choice == 5 :
    break