import random
aArr = []

#0~9까지 랜덤 숫자 추출해서 aArr에 추가

inputCount = 0
while True:
  if inputCount >= 10:
    break
  rand = random.randint(0,9)
  if rand not in aArr:
    aArr.append(rand)
  else:
    continue
  inputCount += 1

# for i in range(10):
#   aArr.append(random.randint(0,9))

print(aArr)


