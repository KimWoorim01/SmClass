import os
import requests
import csv
from bs4 import BeautifulSoup
url = "https://finance.naver.com/sise/lastsearch2.naver"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료

soup = BeautifulSoup(res.text,"lxml")

data = soup.select_one("#contentarea > div.box_type_l > table")

stocks = data.select("tr")

# print(len(stocks))
# sts = stocks[0].select("th")
# st_list = []
# for st in sts:
#   print(st.text.strip())
#   st_list.append(st.text.strip())

st_list = [st.text for st in stocks[0].select("th")]
# print(st_list)
with open("c1023/sto.csv", "w", encoding="utf-8", newline="") as stoFile:
  cWriter = csv.writer(stoFile)
  cWriter.writerow(st_list)
  for idx in range(0,100):
    sto_list = [ sto.text.strip().replace("\t","").replace("\n","") for sto in stocks[idx].select("td")]
    if len(sto_list) <= 1:
      continue

    cWriter.writerow(sto_list)

    if int(sto_list[0]) >= 30:
      break
     
      

# print(sto_list)

