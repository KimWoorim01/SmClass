import requests
from bs4 import BeautifulSoup

url = "http://www.melon.com/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

contents = soup.find("div",{"id":"conts"})
hotData = contents.find("div",{"class":"hot_issue"})
ulList = hotData.find("ul",{"class":"sub_list"})
dlList = ulList.find_all("dl")

for idx,Data in enumerate(dlList) :
  title = Data.find("dt").find("span",{"class":"title"}).text
  print(title)

