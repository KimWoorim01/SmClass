students = [
  [1,'홍길동',100,90,99],
  [2,'유관순',100,100,99],
  [3,'이순신',100,100,99],
  [4,'강감찬',100,90,99],
  [5,'김구',90,90,99]
]

for s in students:
  sum = 0
  for index in range(2,5):
    sum = sum + s[index]
  avg = float("%.2f"%(sum/3))
  s.append(sum)
  s.append(avg)
  s.append(0)


s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

for s in s_title:
  print(s,end='\t')
print(); print("-"*60)

for s in students:
  for i in s:
    print(i,end='\t')
  print()
