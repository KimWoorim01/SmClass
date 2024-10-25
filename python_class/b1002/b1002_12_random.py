import random

# 랜덤숫자 생성 -random
# random() 0<= x <1 실수값을 추출
print(random.random())
print(int(random.random()*10))
print(int(random.random()*10)+1)


print(random.randint(1,3))

# 랜덤 범위 추출 - 1~4 사이 (뒤는 포함 안됨)
print(random.randrange(1,4))

# 리스트에서 랜덤하게 하나 추출
a = [10,20,30,40,50,60,70,80]
print(random.choice(a))

# 리스트에서 여러개 랜덤 추출(중복 가능)
print(random.choices(a, k=2))
