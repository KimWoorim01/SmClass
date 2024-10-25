






# list1 = [52,273,32,72,100]




# try:
#   n_input = int(input("입력할 숫자 >> "))
#   print(f"{n_input}번쨰 리스트 값 : {list1[n_input]}")

# except ValueError as e:
#   print(type(e))
#   print("e : ", e)
  
# except IndexError as e :
#   print(type(e))
#   print("e : ", e)
  
# except Exception as e :           #exception 은 예외 부모 ,예외 처리에서 마지막에 위치해야함
#   print(type(e))
#   print("e : ", e)

# try - except - else - finally
# as e : e 변수는 예외에 대한 설명문, type(e) : 예외 객체
# 리스트 범위 밖 에러 호출 IndexError
# 호출 값 에러 ValueError
#raise 키워드 : 강제예외 발생