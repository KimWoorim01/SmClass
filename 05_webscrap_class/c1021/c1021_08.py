import requests

from bs4 import BeautifulSoup


url = "https://news.naver.com/main/ranking/popularDay.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

wraps = soup.find("div",{"class":"rankingnews_box_wrap _popularRanking"})
Ranks = wraps.find_all("div",{"class":"rankingnews_box"})

with open("c1021/news_test.txt","w",encoding="utf-8") as f:
  for ranklist in Ranks:
    f.write(ranklist.find("strong",{"class":"rankingnews_name"}).text + "\n")
    news = ranklist.find("ul",{"class":"rankingnews_list"})
    newsLists = news.find_all("li")

    for i,newsList in enumerate(newsLists):
      data = newsList.find("a")
      f.write(f"{i+1} : {data.text} + \n")
    f.write("\n")

