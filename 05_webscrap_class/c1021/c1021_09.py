import requests
from bs4 import BeautifulSoup

url = "http://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&xfrom=main^gnb"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

# print(soup.find("div",{"id":"bestPrdList"}).find("h3").text)

bestList = soup.find("div",{"id":"bestPrdList"})

listData = bestList.find("ul",{"class":"cfix"}).find_all("li")
for idx,Data in enumerate(listData) :
  result_Data = Data.find("div",{"class":"pname"}).find("p")
  result_Price = Data.find("strong",{"class":"sale_price"})
  
  print(f"{idx+1}. {result_Data.text}")
  print(f"\t {result_Price.text}")