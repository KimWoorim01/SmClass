# 파일 읽기 - r

students=[]


stu_key = ["no","name","kor","eng","math","total","avg","rank"]

with open("C:/workspace/SmClass/b1016/test3.txt","r",encoding="utf-8") as file:
  while True:
    data = file.readline()
    if not data:
      break
    strData = data.strip().split(",")
    # for i,v in enumerate(strData) :
    #   if i == 1: continue
    #   elif i == 6: v = float(v)
    #   else: v = int(v)
    # students.append(strData)

    strData[0] = int(strData[0])
    strData[1] = strData[1]
    strData[2] = int(strData[2])
    strData[3] = int(strData[3])
    strData[4] = int(strData[4])
    strData[5] = int(strData[5])
    strData[6] = float(strData[6])
    strData[7] = int(strData[7])
    students.append(dict(zip(stu_key,strData)))

    print(data.strip())

print(students)