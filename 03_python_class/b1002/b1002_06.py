students = [
  [1,"홍길동",100,95,91],
  [2,"유관순",90,85,97],
  [3,"이순신",99,99,97]
]

ss = [4,"강감찬",100,90,92]

students.append(ss)

# for stu in students:
#   if stu[1] == "이순신":
#     students.remove(stu)

for i,stu in enumerate(students):
  if stu[1] == "이순신":
    del students[i]


print(students)



# for s in students:
#   if s[1] == "유관순":
#     print(s)

# print(students)
# for s in students:
#   print(s)
