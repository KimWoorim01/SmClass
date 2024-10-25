students = [
  {"no":1,"name":"홍길동","kor":100,"eng":100,"math":99,"total":299,"avg":99.67,"rank":0},
  {"no":2,"name":"유관순","kor":80,"eng":80,"math":85,"total":245,"avg":81.67,"rank":0},
  {"no":3,"name":"이순신","kor":90,"eng":90,"math":91,"total":271,"avg":90.33,"rank":0},
  {"no":4,"name":"강감찬","kor":60,"eng":65,"math":67,"total":192,"avg":64.00,"rank":0},
  {"no":5,"name":"김구","kor":100,"eng":100,"math":84,"total":284,"avg":94.67,"rank":0},
]
s_title = ['번호','이름','국어','영어','수학','합계','평균','등수'] #전역변수
choice = 0 # 전역변수
chk = 0    # 체크변수
count = 1  # 성적처리
stuNo = len(students)  # 리스트에 학생이 있으면, 그 인원으로 변경
no=0;name="";kor=0;eng=0;math=0;total=0;avg=0;rank=0 #성적처리변수




if choice == "4":
  print("[ 학생성적검색 ]")
  name = input("찾고자 하는 학생의 이름을 입력하세요.")
  chk = 0
  sArr = []
  for idx,s in enumerate(students):
    if s["name"].find(name) != -1:
      # 학생출력
      # 상단타이틀 출력
      print(f"{idx}번째, {name} 학생을 찾았습니다")

      sArr.append(s)


      for title in s_title:
        print(f"{title}\t",end="")
      print()
      print("-"*60)
      print(f"{s["no"]}\t{s["name"]}\t{s["kor"]}\t{s["eng"]}\t{s["math"]}\t{s["total"]}\t{s["avg"]:.2f}\t{s["rank"]}\n")
      print()
      chk = 1
  # 모든 학생 비교가 끝난 후, chk 확인
  if chk == 0:
    print(f"{name} 학생이 없습니다. 다시 입력하세요.")
