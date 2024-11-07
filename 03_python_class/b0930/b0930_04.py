
# name = "홍길동"

# print(type(name))

# level = '3레벨'

# print(type(level))

# num = 100
# print(type(num))

# n = 3.14
# print(type(n))

# a_bool = True
# print(type(a_bool))

# a = '100'
# b = "200"
# print(type(a))
# print(type(b))

# print(a+b)
# print(int(a) + int(b))

# c= "3.14"

# print(int(float(c)))

# c = 3.15
# print(str(c))
# print(type(str(c)))

# d = "True"
# print(bool(d))

# 타입변경 - str, float, int , bool


name = input("이름 > ")
kor = input("국어 점수 > ")
eng = input("영어 점수 > ")
math = input("수학 점수 > ")
print("입력 완료!")
print("계산중....")
total = int(kor) + int(eng) + int(math)
avg = "%.2f"%(int(total)/3)

result = f"""\
이름 : {name}, 
국어점수 : {kor}, 
영어점수 : {eng}, 
수학점수 : {math}, 
합계 : {total}, 
평균 : {avg} """

print(result)


