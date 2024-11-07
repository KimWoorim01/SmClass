import requests
from bs4 import BeautifulSoup

url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()


# print(res.text)

soup = BeautifulSoup(res.text,"lxml")

# print(soup.find("h2",{"class":"rankingnews_tit"}))
# print(soup.select_one("h2.rankingnews_tit").text)
# print(soup.select_one("div#header"))
# data = soup.select_one("div.rankingnews_box_wrap")
# news = data.select_one("div.rankingnews_box")

# news_lists = news.select("ul.rankingnews_list>li")
# for idx,news_list in enumerate(news_lists) :
#   print(f"{idx+1}. {news_list.select_one("div.list_content>a").text}")

main_data = soup.select_one("div.rankingnews_box_wrap")
data_list = main_data.select("div.rankingnews_box")

for idx,data in enumerate(data_list) :
  news_lists = data.select("ul.rankingnews_list>li")
  title = data.select_one("strong.rankingnews_name")
  print(title.text)
  for idx,news_list in enumerate(news_lists) :
    print(f"{idx+1}. {news_list.select_one("div.list_content>a").text}")
  print()

