students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]

for s in students:
  sum = 0
  for index in range(2,4):
    sum = sum + s[index]
  avg = float("%.2f"%(sum/3))
  s.append(sum)
  s.append(avg)

print(students)

search = input("이름 입력 >> \n")
findResult = False
for s in students:
  if s[1] == search :
    findResult = True
    print("있음")
    break

if findResult == False :
  print("없음")
