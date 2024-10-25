

students = []
sub = ["no","name","kor","eng","math","total","avg","rank"]

f = open("b1017/subData.txt","r",encoding="utf-8")


while True:
  line = f.readline()
  if not line:break
  s = line.strip().split(",")
  for idx, i in enumerate(s):
    if idx == 1: continue
    elif idx == 6: s[6] = float(i)
    else : s[idx] = int(i)
  students.append(dict(zip(sub,s)))
  # print(s)
  #  students.append(s)
  #  print(line)

print(students)
f.close()
