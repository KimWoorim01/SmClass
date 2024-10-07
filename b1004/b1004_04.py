#두 수를 입력받아, 두수까지 합계를 구하시오

num1 = int(input("숫자 1 입력 >> \n"))
num2 = int(input("숫자 2 입력 >> \n"))
num3 = 0

if num1>num2:
  # num1,num2 = num2,num1
  num3 = num1
  num1 = num2
  num2 = num3

sum = 0
for i in range(num1, num2 + 1):
  sum += i

print(sum)

# num1 = int(input("숫자 1 입력 >> \n"))
# num2 = int(input("숫자 2 입력 >> \n"))

# min_num = min(num1,num2); max_num = max(num1,num2)

# sum = 0
# for i in range(min_num, max_num + 1):
#   sum += i

# print(sum)

# num1 = int(input("숫자 1 입력 >> \n"))
# num2 = int(input("숫자 2 입력 >> \n"))



# sum = 0
# for i in range(num1, num2):
#   sum += i

# print(sum)

#1,3,5,7,9.....99 합계를 구하시오.

# sum = 0
# for i in range(1,100,2):
#   sum += i

# print(sum)


# for i in [1,2,3]:
#   print("Hi"*i)


# for i in range(1,6):
#   print("*"*i)


# for i in range(1,9+1,2):
#   print(f"[  {i}단  ]")
#   for j in range(1,9+1):
#     print(f"{i} x {j} = {i*j}")
#   print("-"*30)



# for i in range(1,10,2):
#   print(i)



# for i in range(1,9+1):
#   print(f"[  {i}단  ]")
#   for j in range(1,9+1):
#     print(f"{i} x {j} = {i*j}")
#   print("-"*30)