
# stu_data =['홍길동',100,94,92,87]

# for s in stu_data:
#   print(s)
titles = ["번호", "이름", "국어", "영어", "수학", "과학", "합계", "평균"]
stu_datas = [
  [1,'홍길동',80,74,92,87],
  [2,'정운룡',90,94,82,87],
  [3,'이순신',100,96,93,85],
  [4,'원균',50,64,32,77]
]

for st in titles:
  print("{}".format(st),end='\t')
print("")
print("*" * 100)

for stu in stu_datas:
  stu_sum = 0
  for s in range(2,6) :
    stu_sum += stu[s]
  stu.append(stu_sum)

for s in stu_datas:
  print("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(s[0], s[1], s[2], s[3], s[4], s[5], s[6], s[6]/4))



# for data in stu_datas:
#   print(
#   """
#   이름: {}
#   국어: {}
#   영어: {}
#   수학: {}
#   과학: {}
#   합계: {}
#   평균: {:.2f}
#   """
#   .format(data[0], data[1], data[2], data[3], data[4], data[5], data[5]/4)
#   )


# sum = 0
# for i in range(1,5):
#   sum += stu_datas[2][i]

# avg = sum/4

# generalData = stu_datas[2]

# print(
# """
# 이름: {}
# 국어: {}
# 영어: {}
# 수학: {}
# 과학: {}
# 합계: {}
# 평균: {:.2f}
# """
# .format(generalData[0], generalData[1], generalData[2], generalData[3], generalData[4], sum, avg)
# )

# sum = 0
# for i in range(1,5):
#   sum += stu_data[i]

# avg = sum/4

# print(
# """
# 이름: {}
# 국어: {}
# 영어: {}
# 수학: {}
# 과학: {}
# 합계: {}
# 평균: {:.2f}
# """
# .format(stu_data[0], stu_data[1], stu_data[2], stu_data[3], stu_data[4], sum, avg)
# )

# print("합계 : {}, 평균 : {:.2f}".format(sum, avg))

# length = input("길이2개 입력 >>")
# print(length)

# lengthList = length.split(" ")
# a, b  = map(int, input('두 숫자 입력 : ').split())
# tri = float(lengthList[0])*float(lengthList[1])/2
# squre = float(lengthList[0])*float(lengthList[1])

# print("삼각형 넓이 : {:.2f}".format(tri))
# print("사각형 넓이 : {:.2f}".format(squre))


# line1 = float(input("변1의 길이 >>"))
# line2 = float(input("변2의 길이 >>"))

# tri = line1*line2/2
# squre = line1*line2

# print("삼각형 넓이 : {:.2f}".format(tri))
# print("사각형 넓이 : {:.2f}".format(squre))


# r = float(input("반지름 길이 입력 :>>"))
# pi = 3.14
# area = r ** 2 * pi
# print("넓이 : {:.2f}".format(area))

# 복합대입 연산자 += , -= , *=, /=, //=, %=, **=
# a = 20
# a +=5; print(a)
# a -=5; print(a)
# a *=5; print(a)
# a /=5; print(a)
# a //=5; print(a)
# a %=5; print(a)
# a **=5; print(a)


# a = 100; b = 10
# print(str(a) + str(b))


# a = "100"
# b = "10.5"
# c = "안녕"
# print(float(a))                   #정수형 -> 정수타입, 실수타입 변환가능
# print(int(b))                   #실수형 -> 실수타입 변환가능
# print(float(c))                   #글자는 숫자형타입으로 변환 불가

# a = 5; b = 3
# a1,a2,a3,a4 = 1,2,3,4


# print(a/b)
# print(a*b)
# print(a%b)
# print(a//b)
# print(a**b)


# print("{:.2f}, {}, {} ,{}, {}".format(a/b, a*b, a%b, a//b, a**b))



# 1,2,3,4,5,6,.....10

# x = 1,2,3,4,5,6,...,10

# print(x)

# x = 11,12,13,14,...,20

# x = 21,22,23,24,...,30






