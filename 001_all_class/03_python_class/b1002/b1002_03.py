inputData = int(input("숫자 입력 >> \n"))

if inputData < 60:
  print("너님 성적:F")
elif 60 <= inputData < 70:
  if 68 <= inputData <= 69:
    print("너님성적: D+")
  elif 64 <= inputData <= 67:
    print("너님성적: D")
  else:
    print("너님성적: D-")

elif 70 <= inputData < 80:
  if 78 <= inputData <= 79:
    print("너님성적: C+")
  elif 74 <= inputData <= 77:
    print("너님성적: C")
  else:
    print("너님성적: C-")

elif 80 <= inputData < 90:
  if 88 <= inputData <= 89:
    print("너님성적: B+")
  elif 84 <= inputData <= 87:
    print("너님성적: B")
  else:
    print("너님성적: B-")
elif 90 <= inputData <= 100:
  if 98 <= inputData <= 100:
    print("너님성적: A+")
  elif 94 <= inputData <= 97:
    print("너님성적: A")
  else:
    print("너님성적: A-")


# inputData = int(input("숫자 입력 >> \n"))

# if 3 <= inputData <=5:
#   print("봄")
# elif 6<= inputData <=8:
#   print("여름")
# elif 9<= inputData <=11:
#   print("가을")
# elif 12 == inputData or 1 <= inputData <= 2:
#   print("겨울")

# inputData = int(input("숫자 입력 >> \n"))

# if 10 <= inputData <= 100:
#   print("정답")
# else:
#   print("오답")


# inputData = int(input("숫자 입력 >> \n"))

# if 1 <= inputData <= 10:              #파이썬만 가능
#   print("정답")
# else:
#   print("오답")
  

# if inputData >= 1 and inputData <=10:
#   print("정답")
# else:
#   print("오답")


# inputData = int(input("숫자 입력 >>  \n"))

# if inputData%2 > 0:
#   print("홀수임")
# else:
#   print("짝수임")