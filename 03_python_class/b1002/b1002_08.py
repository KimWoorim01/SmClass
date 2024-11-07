fruit = ['사과', '딸기', '배', '포도', '복숭아','배','사과','배','딸기']

inputData = input("과일 이름 >> \n")


if inputData in fruit:
  data = []
  count = fruit.count(inputData)
  for index,f in enumerate(fruit):
    if f == inputData:
      data.append(index)
  print("{}은 {}개 있고 위치는 {}".format(inputData,count,data))
else:
  print("{} 없어".format(inputData))




# fruit = ['사과', '딸기', '배', '포도', '복숭아','배','사과','배','딸기']

# inputData = input("과일 이름 >> \n")

# if inputData in fruit:
#   count = fruit.count(inputData)
#   print("{}있고 {}개 있다.".format(inputData,count))
# else:
#   print("없엉")

# fruit = ['사과', '딸기', '배', '포도', '복숭아']

# data = input("과일 입력 >> \n")

# if data in fruit:
#   print("있음")
# else:
#   print("없음")

# fruit = "사과,배,딸기,포도"
# if '' in fruit:
#   print("배 있음")
# else:
#   print("배 없음")