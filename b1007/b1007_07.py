import random

lotto = [0]*6 +[1]*3

random.shuffle(lotto)
a_list = [
  [0,0,1],
  [0,0,0],
  [0,1,0]
]

a_list.clear()
for i in range(3):
  a = []
  for j in range(3):
    a.append(lotto[(i*3)+j])
  a_list.append(a)


aa_list = [
  ["로또","로또","로또"],
  ["로또","로또","로또"],
  ["로또","로또","로또"]
]

print("\t0\t1\t2")
print("-"*30)


while True:
  my_income = int(input("얼마 투자허실? >>  "))
  for i in range(3):
    print(i,"|",end="\t")
    for j in range(3):
      print(aa_list[i][j],end="\t")

    print()

  code = input("좌표를 입력 하세요 (0.0) >>  ")
  if code == "0":
    break
  
  codeArr = code.split(".")
  print(codeArr)
  print(f"{code}좌표의 값 : ",a_list[int(codeArr[0])][int(codeArr[1])])
  if a_list[int(codeArr[0])][int(codeArr[1])] == 0 :
    aa_list[int(codeArr[0])][int(codeArr[1])] = "꽝"
    print("꽝")
  else:
    aa_list[int(codeArr[0])][int(codeArr[1])] = "당첨"
    print(f"*당첨금 {my_income *100:,d}원*")

