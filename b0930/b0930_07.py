titles = ["번호", "이름", "국어", "영어", "수학", "과학", "합계", "평균"]
stu_datas = [
  [1,'홍길동',80,74,92,87],
  [2,'정운룡',90,94,82,87],
  [3,'이순신',100,96,93,85],
  [4,'원균',50,64,32,77],
  [5,'드록바',70,74,52,67]
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

