import requests

res = requests.get("http://www.google.com")         # html 소스 get
# res = requests.get("https://www.melon.com/index.htm")         # html 소스 get
res.raise_for_status()          # 에러시 자동 종료

# requests 정보를 가져올시 
# 제이쿼리, 자바스크립트, 외부페이지, react, ..... 
# 비동기식으로 작동되는 소스는 가져오지 못함


print("총 문자 길이 : ",len(res.text))


# f = open("a.html","w",encoding="utf-8")
# f.write(res.text)
# f.close()

# with open("c1021/a.html","w",encoding="utf-8") as f:
#   f.write(res.text)




# if res.status_code == 200:
#   print(res.text)
# else:
#   print("접근 불가")



# print("응답코드 : ",res.status_code)


# print(res.text)                 #html 소스 출력
