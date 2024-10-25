subject = ["name", "kor", "eng", "math", "sum", "avg"]
students = []


def in_score():

  global subject
  global students
  name = input("이름 입력 >>")
  sum = 0
  score = []
  for i in range(1, len(subject)-2):
    num = int(input(f"{subject[i]} 점수를 입력 >> "))
    score.append(num)
    sum += num
  
  avg = round(sum/len(score),2)
  s = {"name": name, "kor": score[0], "eng":score[1], "math":score[2], "sum":sum, "avg":avg}
  students.append(s)
  return

def out_score(students):

  print(students)
  return

def update_score():
  global students
  global subject

  search = input("학생 이름 검색 >> ")
  find_result = 0
  sum_score = 0
  for s in students:
    if s["name"] == search:
      find_result = 1
      print("[수정 과목 선택]")
      for sub_num in range(1, len(subject)-2):
        print(f"{sub_num}.{subject[sub_num]}",end="\t")

      print()
      choice_sub = int(input("수정할 과목 >> "))
      sum_count = 0
      for sub_index in range(1, len(subject)-2):
        if choice_sub == sub_index:
          new_score = int(input("수정할 점수 입력 >> "))
          s[subject[sub_index]] = new_score
          print(s[subject[sub_index]])
          sum_score += s[subject[sub_index]]
          sum_count += 1
        else:
          sum_score += s[subject[sub_index]]
          sum_count += 1

      s[subject[len(s)-2]] = sum_score
      s[subject[len(s)-1]] = round(sum_score/sum_count,2)
  
  if find_result == 0:
    print("학생을 찾지 못함")
    return

  return

def in_student():
  return

while True:
  print("1. 학생성적 입력")
  print("2. 학생성적 출력")
  print("3. 학생성적 수정")
  print("0. 종료")

  choice = input("항목 선택  >> ")

  if choice == "1" :
    in_score()
  elif choice == "2":
    out_score(students)
  elif choice == "3":
    update_score()
  elif choice == "4":
    in_student()
  elif choice == "0":
    break


