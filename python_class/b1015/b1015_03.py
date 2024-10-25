


# 복합매개변수로 값전달 - 리스트, 딕셔너리, return 으로 a 값 변경해줄 필요가 없다.
def plus(a):
  a[0] = 100
  a[1] = 200
  print("지역변수 a :", a)

a = [10,20]
plus(a)

print("전역변수 a: ", a)


def plus2(b):
  b = 200
  print("b : ",b)
  return b

b =20
print ("start b : ",b)
plus2(b)
print ("end : ",b)


# def plus(a):
#   a = 50
#   a += 20
#   print("1 : ",a)
#   pass

# a = 10

# plus(a)

# print(a)
