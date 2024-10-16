
student = []
s_title = ["번호", "이름", "국어", "영어", "수학", "합계", "평균", "등수"]

choice = 0
chk = 0
count = 1
stuNo = len(student)


def stu_input(stuNo, student) :
  print("[ 학생성적입력]")
  while True:
     stuNo += 1
     name = input(f"{stuNo}번 학생 추가 >> ")
     if name == "end":
       print("종료")
       break
     
     score = []
     for i in range(3):
       data = int(input(f"{s_title[i+2]} 점수 입력"))
       score.append(data)
     
     total = score[0] + score[1] +score[2]
     avg = round(total/3,2)
     rank = 0
     
     s = {"no": stuNo, "name": name, "kor":score[0], "eng":score[1], "math":score[2], "total":total, "avg":avg, "rank":rank}
     student.append(s)

     print(f"{name} 학생 성적이 저장되었음")
  return stuNo


no=0; name = ""; kor = 0; eng = 0; math=0; total = 0; avg = 0; rank = 0


while True:

  print("성적 관리 프로그램")
  print("1. 성적 입력")
  print("2. 성적 출력")

  choice = int(input("원하는 번호를 입력 >>"))

  if choice == 1 :
    stuNo = stu_input(stuNo, student)
    print("현재 학생 번호 : ", stuNo)
  elif choice == 2 :
    print("[성적 출력]")
    print(student)

