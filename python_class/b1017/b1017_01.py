subject = ["국어", "영어", "수학", "과학", "역사"]
score = []

while True:
  print("1.과목추가")
  print("0.종료")
  choice = input("원하는 항목 선택 >> ")
  
  if choice == "1" :
    s_input = input("과목 입력 >> ")
    subject.append(s_input)
  elif choice == "0" :
    break




# for sub in range(len(subject)):
#   score.append(int(input(f"{subject[sub]} 점수 입력 >> ")))


# for s_print in range(len(score)):
#   print(score[s_print])

# score1 = int(input("국어 점수 입력 >> "))
# score2 = int(input("영어 점수 입력 >> "))
# score3 = int(input("수학 점수 입력 >> "))
# score4 = int(input("과학 점수 입력 >> "))
# score5 = int(input("역사 점수 입력 >> "))


# print ("국어 :", score1)
# print ("영어 :", score2)
# print ("수학 :", score3)
# print ("과학 :", score4)
# print ("역사 :", score5)



# subject = ["국어", "영어"]



# def output(subject):

  
#   print("과목")
#   print("-"*30)
#   for s in subject:
#     print(s)



# while True:
#   print("[ 과목 생성 프로그램 ]")
#   print("1. 과목 추가")


#   s_input = input("원하는 과목 입력 >> ")

#   subject.append(s_input)
#   output(subject)



# a = 10
# b = 20
# c = 30
# def func(a,b,c):
#   return a+b+c

# a = func(a,b,c)

# print(a)



# a= 10

# def func():
#   global a

#   a += 10

#   print(a)

# func()

