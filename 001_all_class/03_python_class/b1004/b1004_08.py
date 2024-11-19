s_list = []
s_title = ['번호', '이름', '국어', '영어', '수학', '합계', '평균', '등수']

no = 1
while True:
  print("성적 출력 프로그램")  
  print("-"*60)
  print("1. 성적 입력")
  print("2. 성적 출력")
  print("3. 성적 수정")
  print("4. 종료")
  print("-"*60)
  choice = int(input("항목 선택 >>   "))
  if choice == 1 :
    student= []
    name = input("이름 입력 >>  ")
    kor = int(input("국어점수 입력 >>  "))
    eng = int(input("영어점수 입력 >>  "))
    math = int(input("수학점수 입력 >>  "))
    sum = kor+eng+math
    avg = round(sum/3,2)
    student.append(no)
    student.append(name)
    student.append(kor)
    student.append(eng)
    student.append(math)
    student.append(sum)
    student.append(avg)
    s_list.append(student)
  elif choice == 2 :
    # student_num = int(input("학생번호 입력 >>  ")) -1
    # if s_list[student_num] != "" :
    #   print(s_list[student_num])

    for s in s_title:
      print(s,end='\t')
    print(); print("-"*60)

    for s in s_list:
      for i in s:
        print(i,end='\t')
      print()


  elif choice == 3 :
    print("구현중")
  elif choice == 4 :
    break
  else:
    break
  print("-"*60)







# s_list = []


# no = 1
# while True:
#   name = input("이름 입력 >>  ")
  
#   if name == "0" :
#     print("입력 종료")
#     break
#   student= []
#   kor = int(input("국어점수 입력 >>  "))
#   eng = int(input("영어점수 입력 >>  "))
#   math = int(input("수학점수 입력 >>  "))
#   sum = kor+eng+math
#   avg = round(sum/3,2)
#   student.append(no)
#   student.append(name)
#   student.append(kor)
#   student.append(eng)
#   student.append(math)
#   student.append(sum)
#   student.append(avg)
#   s_list.append(student)
#   no += 1


# print(s_list)