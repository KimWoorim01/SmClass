
sub_Name = ["국어", "영어", "수학"]
score = {"국어":100, "영어":94, "수학":92}

print(score)

print(score[sub_Name[0]])


for k,v in score.items():
  print(k,":",v)










# def dan(start, end):

#   for i in range(start, end+1):
#     print(f"{i}단 ")
#     for j in range(1,10):
#       print(f"{i} * {j} = {i*j}")
#     print("")


# while True:

#   num1 = int(input("구구단 시작 입력 >> "))
  
#   if num1 == 0 :
#     break

#   num2 = int(input("구구단 종료 입력 >> "))


#   dan(num1, num2)
#   print("종료")
