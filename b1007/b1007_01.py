s_list = [
  # [1,'홍길동',100,90,99],
  # [2,'유관순',100,100,99],
  # [3,'이순신',100,100,99],
  # [4,'강감찬',100,90,99],
  # [5,'김구',90,90,99]
]
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']
no = 1




for s in s_list:
  sum = 0
  for index in range(2,5):
    sum = sum + s[index]
  avg = float("%.2f"%(sum/3))
  s.append(sum)
  s.append(avg)
  s.append(0)


while True:
  print("성적 출력 프로그램")  
  print("-"*60)
  print("1. 성적 입력")
  print("2. 성적 출력")
  print("3. 성적 수정")
  print("4. 학생 성적 검색")
  print("5. 종료")
  print("-"*60)
  choice = int(input("항목 선택 >>   "))
  if choice == 1 :

    while True:
      student= []
      name = input(f"{no}번째 이름 입력(0: 메뉴로) >>  ")
      if name == "0" :
        break

      kor = int(input("국어점수 입력 >>  "))
      eng = int(input("영어점수 입력 >>  "))
      math = int(input("수학점수 입력 >>  "))
      sum = kor+eng+math
      avg = round(sum/3,2)
      rank = 0
      student.append(no)
      student.append(name)
      student.append(kor)
      student.append(eng)
      student.append(math)
      student.append(sum)
      student.append(avg)
      student.append(rank)
      s_list.append(student)
      no += 1

  elif choice == 2 :
    for s in s_title:
      print(s,end='\t')
    print(); print("-"*60)

    for s in s_list:
      for i in s:
        print(i,end='\t')
      print()
  elif choice == 3 :
    print("[ 학생 성적 수정 ]")

    b_find = False
    name = input("수정할 이름 입력 >>   ")
    for s in s_list:
      if s[1] == name:
        b_find = True
        print(" [과목 선택] ")
        print("1. 국어점수 ")
        print("2. 영어점수 ")
        print("3. 수학점수 ")
        print("4. 변경 취소 ")
        select = int(input("원하는 과목 선택 >>  "))

        if select == 1 :
          print("현재 국어점수는 : ",s[2])
          s[2] = int (input("수정할 점수 입력 >>  "))
        elif select == 2:
          print("현재 영어점수는 : ",s[3])
          s[3] = int (input("수정할 점수 입력 >>  "))
        elif select == 3:
          print("현재 수학점수는 : ",s[4])
          s[4] = int (input("수정할 점수 입력 >>  "))
        elif select == 4:
          b_find = False
          print("변경 취소")
          break
        else :
          break
        s[5] = s[2] + s[3] + s[4]
        s[5] = round(s[5]/3,2)
        print(f"{name}의 점수 변경 완료")
    if b_find == False:
      print("검색 결과 없음")

  elif choice == 4 :
    print("[ 학생 성적 검색 ]")
    b_find = False
    name = input("검색할 이름 입력 >>   ")
    for s in s_list:
      if s[1] == name:
        b_find = True
        for d in s_title:
          print(d,end='\t')
        print(); print("-"*60)
        for i in s:
          print(i,end='\t')
        print()
        break
    if b_find == False:
      print("검색 결과 없음")
    # students 에 10명
  elif choice == 5 :
    break
  else :
    pass

  print("-"*60)
