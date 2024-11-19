import os
import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
#frm > div > table > thead > tr
lists = soup.select("#frm > div > table > thead > tr")

title = []
tits = lists[0].select("th")

lists = soup.select("#frm > div > table > tbody > tr")

for tit in tits:
  title.append(tit.text.strip())

print(title)

if os.path.exists("c1022/melon") :
  print("있음")
else:
  os.makedirs("c1022/melon")

for i in range(0,5):
  with open(f"c1022/melon/{i}.jpg","wb") as f:

    lis = lists[i].select("td")
    print("순위 :",lis[1].select_one("span").text)
    print("이미지 :",lis[3].select_one("img")["src"])
    img = requests.get(lis[3].select_one("img")["src"])
    f.write(img.content)
    song = lis[5].select("div.ellipsis")
    print("곡정보 :",song[0].select_one("a").text,end="\t")
    singers = song[1].select("a")
    if len(singers) <= 1:
      print(singers[0].text)
    else:
      print(singers[1].text)
      print(singers[2].text)
    # print(song[1].select_one("a").text)
