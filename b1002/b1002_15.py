import random

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