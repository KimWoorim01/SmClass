
all_list = [
  [1,"홍길동",100,90,85],
  [2,"유관순",100,87,92],
  [3,"이순신",100,88,94],
  [4,"강감찬",90,88,79],
  [5,"김구",98,78,84]
]


name = input("이름을 입력하시오 >> \n")


find = False
for data in all_list:
  if data[1] == name:
    print(data)
    find = True
    all_list.remove(data)
    print(all_list)
    break

if find == False:
  print("데이터 없음")


# for data in all_list:
#   if data[1] == "유관순":
#     all_list.remove(data)

# print(all_list)


# aArr = [2,3,4,5,6,7,8,9,10]

# aArr.insert(2,30)
# aArr.remove(6)


# del aArr[0]
# del aArr[2]

# print(aArr)