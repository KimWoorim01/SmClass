import os
import requests
from bs4 import BeautifulSoup
url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=9&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    'Accept-Language' : 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
res = requests.get(url,headers=headers)
res.raise_for_status() # 에러시 종료
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

# 제목, 금액, 평점, 평가수

section = soup.select_one("#searchOptionForm > div.search-wrapper > div.search-content.search-content-with-feedback")
ulList = section.select_one("#productList")
liList = ulList.select("li.search-product")
# print(liList)
passingData = []
productData = []
for listIndex in range(0,len(liList)):
  print()
  linkData = liList[listIndex].select_one("a.search-product-link")["href"]

  if linkData is None:
    passingData.append(listIndex)
    continue
  nameData = liList[listIndex].select_one("div.name")
  
  if nameData is None:
    passingData.append(listIndex)
    continue
  priceData = liList[listIndex].select_one("div.price-wrap")
  
  if priceData is None:
    passingData.append(listIndex)
    continue
  strPrice = priceData.select_one("strong.price-value").text.strip()
  
  imgData = liList[listIndex].select_one("img.search-product-wrap-img")
  if imgData is None:
    passingData.append(listIndex)
    continue

  ratingData = liList[listIndex].select_one("div.rating-star")
  if ratingData is not None :
    ratingStar = ratingData.select_one("span.star").text.strip()
    ratingCount = ratingData.select_one("span.rating-total-count").text.strip()

    if int(ratingCount.replace("(","").replace(")","")) >= 50 :
      print(f"링크 : http:/{linkData.strip().replace("\t","")}")
      print(f"제목 :{nameData.text.strip()},\n가격 :{strPrice},\n평점 :{ratingStar} , 평가수:{ratingCount.replace("(","").replace(")","")}")
      print(f"이미지 : http:{imgData["src"].strip()}")
      
      mapData = {
        "link" : f"http:/{linkData.strip().replace("\t","")}",
        "name" : f"{nameData.text.strip()}",
        "price" : int(strPrice.strip().replace(",","")),
        "rating" : float(ratingStar),
        "ratingCount" : int(ratingCount.replace("(","").replace(")",""))
      }
      productData.append(mapData)
    else:
      passingData.append(listIndex)
      continue

  else:
    passingData.append(listIndex)
    continue
    # print("링크 : ",linkData)
    # print(f"제목 :{nameData.text.strip()},\n가격 :{priceData},\n평점 :0 , 평가수:0")
# print(passingData)
# print(productData)

# n_lists.sort(key=lambda x:x[0],reversed=True)


while True:
  print("[ 노트북 비교 ]")
  print("1. 금액 정렬")
  print("2. 금액 역순정렬")
  print("3. 평점 정렬")
  print("4. 평점 역순정렬")
  print("0. 종료")

  choice = input("원하는 항목 선택 >> ")

  if choice == "0" :
    break
  elif choice =="1" :
    productData.sort(key=lambda x:x["price"],reverse=True)
    for data in productData:
      print(f"이름:{data["name"]} , 가격:{data["price"]} , 평점:{data["rating"]}")
    pass
  elif choice =="2" :
    productData.sort(key=lambda x:x["price"],reverse=False)
    for data in productData:
      print(f"이름:{data["name"]} , 가격:{data["price"]} , 평점:{data["rating"]}")
    pass
  elif choice =="3" :
    productData.sort(key=lambda x:x["rating"],reverse=True)
    for data in productData:
      print(f"이름:{data["name"]} , 가격:{data["price"]} , 평점:{data["rating"]}")
    pass
  elif choice =="4" :
    productData.sort(key=lambda x:x["rating"],reverse=False)
    for data in productData:
      print(f"이름:{data["name"]} , 가격:{data["price"]} , 평점:{data["rating"]}")
    pass
