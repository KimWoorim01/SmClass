import random

fName = ["바나나", "오렌지", "체리", "파인애플", "코코넛"]
fruit = {"바나나" : "banana", "오렌지":"orange", "체리":"cherry", "파인애플":"pineapple", "코코넛":"coconut"}


re_fName = random.sample(fName,5)


for i in re_fName:
  search = input(f"{i}의 영문을 입력하세요")
  if fruit[i] == search:
    print("정답임 ",fruit[i], search)
  else :
    print("오답임 ",fruit[i], search)


# print("[영단어 맞추기]")
# for key in fruit.keys():
#   search = input(f"{key}의 영문을 입력하세요")
#   if fruit[key] == search:
#     print("정답임 ",fruit[key], search)
#   else :
#     print("오답임 ",fruit[key], search)

# fruit_name = input("과일 이름 입력 >> ")

# result = fruit[fruit_name]

# print(result)