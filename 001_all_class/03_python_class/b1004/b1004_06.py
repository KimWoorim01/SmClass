
a_list = ["홍길동", "유관순", "이순신"]

a_list = [ a + "님" for a in a_list]

print(a_list)

# a_list = [1,2,3,4,5]

# 리스트의 값을 변경해서 리스트에 저장 - 리스트 내포, 한줄 for문
# a_list = [a+2 for a in a_list]

# for index,a in enumerate(a_list):
#   a_list[index] = a**2

# print(a_list)
# print(a_list[0:4])

# # 리스트 범위 넘어서 출력하면 에러가 나지 않고 출력은 된다. 단, 있는 범위까지만
# print(a_list[0:10])

# print(a_list)

# a_list[1] = 100

# print(a_list[1])

# b_list = [1*1, 2*2, 3*3, 4*4, 5*5]

# print(a_list)
# print(b_list)



# a_list = ['홍길동', '유관순', '이순신', '강감찬', '김구', '김유신', '홍길자']

# for a in a_list :
#   print(a)

# enumerate() 함수 - index 번호를 출력 index, value
# for i,a in enumerate(a_list):
#   print(f"{i+1}:{a}")