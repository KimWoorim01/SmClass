import random

#25개 1차원 리스트

#25개 중 1을 5개 나머지는 0으로 입력해서 출력하시오?

a_list = [0]*20 + [1]*5

random.shuffle(a_list)

print(a_list)
c_list = a_list[:]
a_list.clear()
for i in range(5):
  f_list = []
  for j in range(5):
    f_list.append(c_list[(5*i)+j])
  a_list.append(f_list)


while True:
  print("\t0\t1\t2\t3\t4")
  
  for i in range(5):
    print(i, end="\t")
    for j in range(5):
      print(a_list[i][j],end="\t")
    print()
  data = input("좌표를 입력하세요. >>[0,1]  ")
  data1 = data.split(",")
  print(data1)
  print(f"{data} 좌표의 값", a_list[int(data1[0])][int(data1[1])])


  
# a_list = []
# for i in range(25):
#   if i<5:
#     a_list.append(1)
#   else:
#     a_list.append(0)

# print(a_list)



