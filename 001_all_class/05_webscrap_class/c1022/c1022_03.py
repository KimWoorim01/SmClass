import requests
from bs4 import BeautifulSoup

url = "http://finance.naver.com/"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

res = requests.get(url,headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")


# print(soup.select_one("h3.h_popular>span").text)

data = soup.select_one("#container > div.aside > div > div.aside_area.aside_popular")

print(data.select_one("span").text)
print()
pops = data.select("tbody>tr")
#next_sibling : 형제관계 , find_next_sibling : 형제관계중 검색
sum = 0
for idx, trData in enumerate(pops):
  next_span = trData.select_one("span.tah").text.strip()
  print(f"{trData.select_one("a").text}\t{trData.select_one("td").text}\t\t{next_span}\t{trData.select_one("span").text}")
  sum += int(trData.select_one("td").text.strip().replace(",",""))
  print()
print(sum)