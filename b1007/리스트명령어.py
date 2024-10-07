
a_list = [1,2,3,4,5,6]

print(len(a_list))

del(a_list[3])
print(a_list.remove(5))

print(a_list.count(3))
a_list.insert(0,100)
a_list.clear()


# a_list = [1,2,3,4,5]
# del a_list[0]

# print(a_list)
# a_list[1:3] = []
# print(a_list)

# a_list = None       #전체삭제
# a_list = [3,4,5,8,7]
# a_list = []         #전체 삭제
# a_list = [3,4,5,8,7]
# print(a_list)

# del(a_list)         #del로 삭제하면 a_list 자체가 날아감


# a_list = [1,2,3,4,5,6,7]
# a_list[3] = 50
# a_list[1:2] = [20,30]


# print(a_list)


# a_list = [1,2,3,4,5]
# b_list = a_list[:]

# print(a_list[0:5])
# print(a_list[2:4])
# print(a_list[:3])
# print(a_list[3:])
# print(a_list[2:5])
# print(a_list+b_list)
# print(b_list*3)

# print(a_list[::2])
# print(a_list[::-2])
# print(a_list[::-1])



# a_list = [1,2,3,4,5]
# b_list = a_list               # 얕은 복사 (주소값만 복사)

# a_list[0] = 100

# print(a_list)
# print(b_list)

# b_list = a_list[:]        #깊은 복사
# a_list[0] = 10            
# print(a_list)
# print(b_list)


# a_list = [1,2,3,4,5]
# b_list = a_list[::-1]
# print(a_list)
# print(b_list)
# a_list[0] = 100
# print(a_list)
# print(b_list)




# a_list = [5,2,3,4,5]
# for i in a_list:
#   print(i)


# # 역순 출력
# for i in range(len(a_list)):
#   print(a_list[-(i+1)])

# # 역순 출력
# for i in range(1,len(a_list)+1):
#   print(a_list[-i])

# a_list = [1, 2, 3.0, "안녕", True, False]

# print(a_list[0])
# print(a_list[3])
# print(a_list[-1])



# a_list= []

# for i in range(100):
#   a_list.append(i+1)

# print(a_list)



# a_list = []
# total = 0

# for i in range(10):
#   j = int(input(f"{i + 1}번째 숫자를 입력 >> "))
#   a_list.append(j)
#   total += j




# total = 0
# a_list = [0,0,0,0,0,0,0]
# for idx,a in enumerate(a_list):
#   a = int(input(f"{idx}번째 숫자 입력 요망 >>  "))
#   total += a


# a_list = [0,0,0,0,0,0,0]
# total = 0
# for a in a_list:
#   a = int(input("숫자 입력 요망 >>  "))
#   total += a

# print("합계 : ",total)

# a,b,c,d,e,f,g = 0,0,0,0,0,0,0
# total = 0

# a = int(input("숫자 입력 요망 >>  "))
# print()
# b = int(input("숫자 입력 요망 >>  "))
# print()
# c = int(input("숫자 입력 요망 >>  "))
# print()
# d = int(input("숫자 입력 요망 >>  "))
# print()
# e = int(input("숫자 입력 요망 >>  "))
# print()
# f = int(input("숫자 입력 요망 >>  "))
# print()
# g = int(input("숫자 입력 요망 >>  "))
# print()

# total = a+b+c+d+e+f+g
# print ("합계 : ",total)
