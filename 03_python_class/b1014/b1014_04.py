

def calc_num(num1,num2,op):
  result = 0
  if op == "+":
    result = num1 + num2
  elif op == "-":
    result = num1 - num2
  elif op == "*":
    result = num1 * num2
  elif op == "/":
    result = num1 / num2

  return result

while True:
  op = input("+,-,*,/ 하나 선택 >> ")
  if op == "end":
    break
  
  num1 = int(input("숫자 입력 >> "))
  num2 = int(input("숫자 입력 >> "))

  result = calc_num(num1,num2,op)

  print("결과값 : ",result)


