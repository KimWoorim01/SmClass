import os
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


for i in range(5):
  url = f"https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EB%A6%89&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=false&page={i}"
  browser = webdriver.Chrome()
  browser.get(url)
  time.sleep(3)
  soup = BeautifulSoup(browser.page_source,"lxml")

  with open(f"c1023/yeogi_{i+1}_test.html","w",encoding="utf-8") as f:
    f.write(soup.prettify())


for i in range(5):
  with open(f"c1023/yeogi_{i+1}_test.html","r",encoding="utf-8") as f:
    soup = BeautifulSoup(f,'lxml')

  data = soup.select_one("#__next > div > main > section > div.css-1qumol3")

  dataLists = data.select("a")
  # print(len(dataLists))

  for idx, sell in enumerate(dataLists):
    productName = sell.select_one("div.css-8fn780>h3").text.strip()
    ratingPoint = sell.select_one("span.css-9ml4lz").text.strip()
    nRatingPoint = float(ratingPoint)
    rating = sell.select_one("span.css-oj6onp").text.strip()[:-4]
    nRating = int(rating.replace(",",""))

    priceRoot = sell.select_one("span.css-5r5920")
    if priceRoot == None :
      continue
    price = sell.select_one("span.css-5r5920").text.strip().replace(",","")
    print(f"상품 : {productName}, 평점 : {ratingPoint}, 평가수 : {rating}, 가격 : {price}")
  print("*"*80)

  # print(data)


# Chrome() 안에 chromedriver.exe 위치 지점을 입력해줘야 함(원래는)
# root에 파일 저장되어 있으면 입력 안해도 된다.
# browser = webdriver.Chrome()
# browser.get(url)
# soup = BeautifulSoup(browser.page_source,"lxml")

# with open("c1023/1023_05_sub.html","w",encoding="utf-8") as f:
#   f.write(soup.prettify())

# data = soup.select_one("#__next > div > main > section > div.css-1qumol3")
# print(data)

# with open("c1023/1023_05_sub.html","r",encoding="utf-8") as f:
#   soup = BeautifulSoup(f,'lxml')


# data = soup.select_one("#__next > div > main > section > div.css-1qumol3")

# dataLists = data.select("a")
# # print(len(dataLists))

# for idx, sell in enumerate(dataLists):
#   productName = sell.select_one("div.css-8fn780>h3").text.strip()
#   ratingPoint = sell.select_one("span.css-9ml4lz").text.strip()
#   nRatingPoint = float(ratingPoint)
#   rating = sell.select_one("span.css-oj6onp").text.strip()[:-4]
#   nRating = int(rating.replace(",",""))

#   priceRoot = sell.select_one("span.css-5r5920")
#   if priceRoot == None :
#     continue
#   price = sell.select_one("span.css-5r5920").text.strip().replace(",","")
#   print(f"상품 : {productName}, 평점 : {ratingPoint}, 평가수 : {rating}, 가격 : {price}")

# print(data)









# requset 정보 가져오기
# url = "https://www.yeogi.com/domestic-accommodations?keyword=%EA%B0%95%EC%9B%90%EB%8F%84&autoKeyword=&checkIn=2024-10-23&checkOut=2024-10-24&personal=2&freeForm=true"
# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
#     'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}

# res = requests.get(url,headers=headers)
# soup = BeautifulSoup(res.text,"lxml")


# with open("c1023/yeogi1.html","w",encoding="utf-8") as f:
#   f.write(soup.prettify())


# data = soup.select_one("#__next > div > main > section > div.css-1qumol3 > a:nth-child(3) > div > div.css-7xiv94 > div.css-nl3cnv > img")
# print(data)