

s_list = []
no = 1
while True:
  name = input("이름 입력 >>  ")
  kor = int(input("국어 점수 입력 >>  "))
  eng = int(input("영어 점수 입력 >>  "))
  math = int(input("수학 점수 입력 >>  "))
  print(f"번호 : {no}, 이름 : {name}, 국어 : {kor}, 영어 : {eng}, 수학 : {math}, 합계 : {kor + eng + math}, 평균 : {(kor+eng+math)/3:.2f}")
  no += 1



  
# while True :
#   num = int(input("숫자를 입력 >> \n"))
#   num2 = int(input("숫자를 입력2 (종료는 0) >> \n"))

#   if num2 == 0 :
#     break

#   print("[두수의 사칙연산]")
#   print("-"*50)

#   print("1. 두수 더하기")
#   print("2. 두수 빼기")
#   print("3. 두수 곱하기")
#   print("4. 두수 나누기")
#   print("-"*50)

#   choice = int(input("원하는 번호 입력 >> \n"))
#   if choice == 1:
#     print(num + num2)
#   elif choice == 2:
#     print(num - num2)
#   elif choice == 3:
#     print(num * num2)
#   elif choice == 4:
#     print(num / num2)
#   else :
#     break
    
# sum = 0
# while True:
#   num1 = int(input("숫자 입력 >> \n"))
#   if num1 == 0 :
#     print(sum)
#     break
#   sum += num1



# i = 0
# while True:
#   print(i)
#   i += 1



# i = 0
# while(i < 10):
#   print(i)
#   i += 1

