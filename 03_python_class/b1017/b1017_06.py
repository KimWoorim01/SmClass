a = ['20','Amata','52','52','57','161','53']
b = ['13','44','58','87','67','212','70']


def f_float(value):
  if value.isdigit() :
    return int(value)
  else :
    try:
      return float(value)         #실수일때 실수 반환
    except:
      return value                #문자열일때 문자열 그대로 리턴


c = []

for idx,vlaue in enumerate(a):
  c.append(f_float(vlaue))

print(c)

for i in b:
  c.append(float(i))

# print(c)

for idx,i in enumerate(a):
  if i.isdigit():
    print(f"{idx}\t숫자입니다")
  else :
    print(f"{idx}\t문자입니다")




