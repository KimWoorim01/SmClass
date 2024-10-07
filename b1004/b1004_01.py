students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]

for student in students:
  sum = 0
  avg = 0
  for index in range(2,5):
    sum += student[index]
  avg = float("%.2f"%(sum/3))
  student.append(sum)
  student.append(avg)
  print(student)

# print(students)
