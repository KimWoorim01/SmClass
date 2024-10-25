import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_quant.naver?sosok=0"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")
tbodyData = soup.select_one("#contentarea > div.box_type_l>table")

# print(tbodyData)
with open("c1022/finance_01.txt","w",encoding="utf-8") as financeFile:
  data = tbodyData
  
  strDatas = data.select("th")
  for i,strData in enumerate(strDatas):
    financeFile.write(f"{strData.text}\t")
    print(f"{strData.text}",end="\t\t")
  financeFile.write("\n")
  strDatas = data.select("tr")


  for idx,trData in enumerate(strDatas):
    if idx == 0:
      continue
    else :
      financeFile.write("\n")
      for tdidx,tdData in enumerate(trData):
        if len(tdData) >1 & len(tdData) == 0 :
          continue
        # print(len(tdData))
        financeFile.write(f"{tdData.text.strip().replace("\n","").replace("\t","")}\t")
        # financeFile.write(f"{tdData.text.strip()}\t")
        # print(f"{tdData.text.strip()}",end="\t\t")

  
    



