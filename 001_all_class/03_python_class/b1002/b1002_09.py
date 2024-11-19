# fruit = ['사과', '딸기', '배', '포도', '복숭아','배','사과','배','딸기']
fruit = '사과,딸기,배,포도,복숭아,배,사과,배,딸기'

fruits = fruit.split(",")
print(fruits)
inputData = input("과일 입력 >> \n")

if inputData in fruits:
  data = []
  count = fruits.count(inputData)
  for index,f in enumerate(fruits):
    if f.find(inputData) >= 0:
      data.append(index)
  print("{}은 {}개 있고 위치는 {}".format(inputData,count,data))
else:
  print("{} 없어".format(inputData))