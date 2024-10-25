fruit = []

while True:
  search = input("과일 이름 입력 >> \n").strip()
  search.replace(" ", "")
  if(search == 'x'):
    break
  else:
    if search in fruit:
      print("이미 있음")
    else:
      fruit.append(search)
    
print(fruit)
