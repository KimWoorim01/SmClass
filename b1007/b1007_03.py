
result_list = []


for i in range(0, 5) :
  m_list = []
  for j in range(0, 5):
    m_list.append((5*i)+j+1)

  result_list.append(m_list)

print(result_list)

# a_list = []

# for i in range(9):
#   a_list.append(i+1)

# b_list = []

# for i in range(9) :
#   b = []
#   if (a_list[i]%4) == 0 :
#     b.append(a_list[i])

# print(b_list)

# a_list = []

# for i in range(0,3):
#   a = []
#   for j in range(0,3):
#     a.append((3*i)+j+1)    
#   a_list.append(a)
# print(a_list)

# a_list = [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ]

# b_list = []

# for i in a_list :
#   for j in i :
#     b_list.append(j)

# print(b_list)


# 2차원 리스트
# a_list = [
#   [1,2,3,4],
#   [5,6,7,8],
#   [9,10,11,12]
# ]


# for i in a_list :
#   for j in i :
#     print(j)
