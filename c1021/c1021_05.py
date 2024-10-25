import requests
from bs4 import BeautifulSoup



url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

print(soup.title)       #제일먼저 찾아지는것 출력
print(soup.find("title"))             #특정 위치의 태그 출력
print(soup.find("title",{"class":"rankingnews_wrap"}))             #특정 위치의 태그 출력

print(soup.find("div",{"class":"rankingnews_box"}))
print(len(soup.find_all("div",{"class":"rankingnews_box"})))

#rankingnews_wrap = soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})
news_list = soup.find("div",{"class":"rankingnews_box_wrap"}).find_all("div",{"class":"rankingnews_box"})
newslist = soup.find("div",{"class":"rankingnews_box_wrap"}).find("div",{"class":"rankingnews_box"})
rankingnews_boxs = soup.find("div",{"class":"rankingnews_box"})

print(len(news_list))
print(1,"="*20)


#next : 검색 태그 다음 뒤에 오는 태그를 찾아줌
#next_sibling : 검색 태그 다음
print(newslist.next_sibling.next_sibling)


# for news in news_list:
#   print(news.find("strong",{"class":"rankingnews_name"}))

# print(len(rankingnews_wrap))

# print(len(soup.find_all("strong",{"class":"rankingnews_name"})))



