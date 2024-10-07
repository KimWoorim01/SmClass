import random





a_list= []

for i in range(25):
  a_list.append(i+1)


random.shuffle(a_list)

b_list = []
for i in range(0,len(a_list),5):
  b_list.append(a_list[i:i+5])


while True:
  print("\t0\t1\t2\t3\t4")
  
  for i in range(5):
    print(i, end="\t")
    for j in range(5):
      print(b_list[i][j],end="\t")
    print()
  data = input("좌표를 입력하세요. >>[0,1]  ")
  data1 = data.split(",")
  print(data1)
  print(f"{data} 좌표의 값", b_list[int(data1[0])][int(data1[1])])


# print(b_list)
# print(a_list)


# result_list = []

# middle_list = []

# while len(middle_list) < 25:
#   num = random.randint(1,25)
#   if num not in middle_list:
#     middle_list.append(num)

# print(middle_list)


# a_list = []
# for idx,data in enumerate(middle_list) :
#   if (idx+1)%5 == 0 :
#     result_list.append(a_list)
#     a_list.clear()
#   else:
#     a_list.append(data)



# for i in range(5):
#   a = []
#   for j in range(5):
#     a.append(middle_list[5*i+j])
#   result_list.append(a)

# print(result_list)