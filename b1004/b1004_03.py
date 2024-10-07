

for i in range(10):
  print(i)
print("-"*60)

for j in range(5,10):
  print(j)


a_list = [1,2,3,4,5]
for k in a_list:
  print(k)


b_list = [3,5,5,5,7,10,20]

for m in b_list:
  print(m)

# 파이썬 - 문자열-str, 정수형-int , 실수형-float, 논리형-bool
# 리스트타입 - []
# 딕셔너리 타입 - {} : json 타입과 모양이 같음. 키,값(key, value)
dic = {
  "번호":1,
  "이름":"이순신",
  "국어":100,
  "영어":90,
  "수학":94
}



print(len(b_list))
print(b_list.count(5))


# 리스트 추가 - append, insert, extend([2,4,5])- 리스트를 추가
# 리스트 삭제 - del, remove, clear-모두 삭제