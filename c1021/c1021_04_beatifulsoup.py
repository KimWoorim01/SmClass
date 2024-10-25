
import requests

from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

# html, css 정보를 가진 소스변경
soup = BeautifulSoup(res.text,"lxml")

print(soup.title)           #index 가 아니라 원하는 정보를 바로 찾을수 있음

#두개가 똑같다
print(soup.title.get_text())
print(soup.title.text)

# print("없는 태그 : ",soup.titletitletitle)                #에러가 발생하지 않고 none 를 return함
# print("없는 태그 : ",soup.titletitletitle.get_text())     #에러 발생

print(soup.a)
print(soup.a.next.text)             #next 다음 태그를 가져옴
print(soup.a.attrs)                 #태그 속성값 가져옴 : 딕셔너리 형태
# print(soup.a["herf"])               #태그 href 속성값 가져옴


#특정 정보를 출력

print(soup.find("div",attrs={"id":"header"}))                         #div태그 id="header"
print(soup.find("h2",attrs={"class":"rankingnews_tit"}))              #h2 태그 class="rankingnews_tit" 
# print(soup.find_all("div"))                                      #모든 div태그 검색
print(type(soup.find_all("div")))                                      #모든 div태그 타입
# print(len(soup.find_all("div")))                                      #모든 div태그 갯수

# with open("c1021/test_04.html","w",encoding="utf-8") as f :
#   # soup.prettif() : 소스가 정리되어 저장됨.
#   f.write(soup.prettify())



