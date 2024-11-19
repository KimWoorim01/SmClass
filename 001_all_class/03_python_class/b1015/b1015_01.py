



# 함수 - 가변매개변수, 키워드 매개 변수 동시 사용할 경우
# def plus(*n, k=10):
#   for i in n:
#     print(i)
#   print(k)


# plus(1,2,3,4,5,99)


# print(1,2,3,4,5,sep=" ", end="\t")
# print(4515)




# def plus(k = 10 , m = 5):

#   print(k)
#   print(m)


# plus(5)

# 가변 매개 변수는 항상 마지막에 사용 해야 한다.
# def plus(a, *n1):

#   for i in n1:
#     print(i)

#   print(type(n1))
#   print(a)

# plus(1,2,3,4,5)




# 가변 매개 변수
# def plus(*n1):

#   for i in n1:
#     print(i)

#   print(type(n1))

# plus(1,2,3,4,5)


# def plus(n1, n2):
#   sum = n1 + n2
#   print("합계 : ", sum)
#   return sum


# plus (10,20)



# def calc(st, end):

#   for i in range(st,end+1):
#     print(f"[ {i}단 ]")
#     for j in range(1,10):
#       print(f"{i} * {j} = {i*j}")



#   pass


# st = 1
# end = 5

# calc(st, end)
