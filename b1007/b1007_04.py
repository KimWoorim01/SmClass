import random


a_list = []

while len(a_list) < 25:
  randNum = random.randint(1,25)
  if randNum not in a_list:
    a_list.append(randNum)

print(a_list)



b_list = random.choices(a_list, k=10)               # 중복 됨
print(b_list)

# b_list = random.sample(a_list,10)             # 중복 안됨
# print(b_list)


# num = int(random.random()*25)+1
# a_list = []
# for i in range(25):
#   randNum = random.randint(1,25)

#   if randNum not in a_list:
#     a_list.append(randNum)
    


# print(a_list)

