import requests
from bs4 import BeautifulSoup

url = "https://www.melon.com/chart/index.htm"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

#순위, 사진링크주소, 제목, 가수명

mainData = soup.select_one("#frm > div > table > tbody")
trData = mainData.select("tr")

tdData = trData[0].select("td")
# print(tdData)

datalist = []
aList = []
#lst50 > td:nth-child(4) > div > a > img
# print(soup.find("h2",attrs={"class":"rankingnews_tit"})) 
with open("c1022/album.txt","w",encoding="utf-8") as albumFile:

  for i in range(0,len(trData)):
    tdData = trData[i].select("td")
    for idx,data in enumerate(tdData):
      if idx == 1:
        datalist.append(data.text.strip().replace("\t","").replace("\n",""))
      elif idx == 3:
        datalist.append(data.select_one("div>a>img")["src"].strip().replace("\t","").replace("\n",""))
      elif idx == 5:
        aLists = data.select("a")
        for aData in aLists:
          aList.append(aData.text.strip().replace("\t","").replace("\n",""))
      else:
        continue
    albumFile.write(f"순위:{datalist[0]}, 이미지주소 :{datalist[1]}, 제목: {aList[0]}, 가수: {aList[1]}\n")
    datalist.clear()
    aList.clear()
