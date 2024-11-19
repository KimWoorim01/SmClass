





while True:

  no = int(input("번호를 입력 >> "))

  if no == 0 :
    break
  name = input("이름를 입력 >> ")
  kor = int(input("국어 점수를 입력 >> "))
  eng = int(input("영어 점수를 입력 >> "))
  math = int(input("수학 점수를 입력 >> "))

  total = kor + eng + math
  avg = round(total/3,2)
  rank = 0

  data = f"{no},{name},{kor},{eng},{math},{total},{avg},{rank}"

  with open("C:/workspace/SmClass/b1016/test3.txt","a",encoding="utf-8") as file:
    file.write(data + "\n")

