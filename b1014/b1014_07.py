stu_title = ["국어", "영어", "수학"]
student = {"국어":100, "영어":95, "수학":95, "합계":290}

print("[점수조정]")
print("1.국어")
print("2.영어")
print("3.수학")

choice = int(input("수정하려는 과목을 선택하세요. >>  "))

if choice == 1 :
  print("현재 국어점수 : ", student[stu_title[0]])
  student[stu_title[0]] = int(input(stu_title[0]," 점수를 입력하세요"))

elif choice == 2 :
  print("현재 영어점수 : ", student[stu_title[1]])
  student[stu_title[1]] = int(input(stu_title[1]," 점수를 입력하세요"))
  
elif choice == 3 :
  print("현재 국어점수 : ", student[stu_title[2]])
  student[stu_title[2]] = int(input(stu_title[2]," 점수를 입력하세요"))

student["합계"] = student["국어"] + student["수학"] + student["영어"]

print("변경 ",student)


