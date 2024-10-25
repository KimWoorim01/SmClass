import random

# 1-100 까지의 랜덤숫자 생성
# 입력한 숫자가 랜덤 숫자보다 크면 입력한 숫자가 큽니다.
# 입력한 숫자가 랜덤 숫자보다 작으면 입력한 숫자가 작습니다.

count = 0

goal = random.randint(0,100)
while True:
  if count >= 10 :
    print("횟수 초과")
    break
  answer = int(input("숫자 입력 요망 >> \n"))
  if answer > goal:
    print("숫자가 큼")
  elif answer < goal:
    print("숫자가 작음")
  elif answer == goal:
    print("정답 {}회째".format(count))
    break
  count += 1

# matching = False
# for i in range(10):
#   answer = int(input("숫자 입력 요망 >> \n"))
#   if answer > goal:
#     print("숫자가 큼")
#   elif answer < goal:
#     print("숫자가 작음")
#   elif answer == goal:
#     matching = True
#     print("정답 {}회째".format(i))
#     break

# if matching == False :
#   print("횟수 초과")
