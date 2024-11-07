from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import time
import requests
import random
import pyautogui
import csv

def data_Search1(dataList, saveList, errorList):
  
  for idx,products in enumerate(dataList):
    idx += 1

    getPrevClass = "div.adProduct_inner__W_nuz > div.adProduct_info_area__dTSZf > "
    productName = products.select_one(f"{getPrevClass} div.adProduct_title__amInq > a")
    
    if productName is None:
      print("data_search1 error -nameless")
      errorList.append(idx)
      continue

    productPrice = products.select_one(f"{getPrevClass} div.adProduct_price_area__yA7Ad >strong.adProduct_price__9gODs > span.price > span.price_num__S2p_v > em")
    if productPrice is None:
      print("data_search1 error -priceless")
      errorList.append(idx)
      continue

    ratingList = products.select_one(f"{getPrevClass} div.adProduct_etc_box__UJJ90 > span.adProduct_etc___brfw > a")

    if ratingList is None:
      print("data_search1 error -ratinglist is none")
      errorList.append(idx)
      continue
    
    ratingStar = ratingList.select_one("span.adProduct_rating__PaMzh")
    if ratingStar is None:
      print("data_search1 error -ratingstar is none")
      errorList.append(idx)
      continue

    ratingCount = ratingList.select_one("em.adProduct_count__EDNPm")
    if ratingCount is None:
      print("data_search1 error -ratingcount is none")
      errorList.append(idx)
      continue

    data =[]
    data.append(productName.text.strip())
    data.append(productPrice.text.strip().replace("원","").replace(",",""))
    data.append(float(ratingStar.text.strip().replace("별점","")))
    data.append(int(ratingCount.text.strip().replace(",","").replace("(","").replace(")","").replace(".","").replace("만","")))
    
    # data = {
    #   "이름" : f"{productName.text.strip()}",
    #   "가격" : f"{productPrice.text.strip().replace("원","").replace(",","")}",
    #   "별점" : f"{float(ratingStar.text.strip().replace("별점",""))}",
    #   "리뷰" : f"{int(ratingCount.text.strip().replace(",","").replace("(","").replace(")","").replace(".","").replace("만",""))}"
    # }
    saveList.append(data)
    print(f"이름 : {productName.text.strip()} , 가격 : {productPrice.text.strip()} , 별점 : {ratingStar.text.strip().replace("별점","")}, 리뷰 : {ratingCount.text.strip()}")
  
  # print(f"error List \n {errorList}")

  # print(saveList)



def data_Search2(dataList, saveList, errorList):
  
  for idx,products in enumerate(dataList):
    idx += 1

    getPrevClass = "div.product_inner__gr8QR > div.product_info_area__xxCTi > "
    productName = products.select_one(f"{getPrevClass} div.product_title__Mmw2K")
    
    if productName is None:
      print("data_search2 error -nameless")
      errorList.append(idx)
      continue

    productPrice = products.select_one(f"{getPrevClass} div.product_price_area__eTg7I >strong.product_price__52oO9 > span.price > span.price_num__S2p_v > em")
    if productPrice is None:
      print("data_search2 error -prceless")
      errorList.append(idx)
      continue

    ratingList = products.select_one(f"{getPrevClass} div.product_etc_box__ElfVA")

    if ratingList is None:
      print("data_search2 error -ratinglist is none")
      errorList.append(idx)
      continue
    
    ratingStar = ratingList.select_one("span.product_grade__IzyU3")
    if ratingStar is None:
      print("data_search2 error -ratingstar is none")
      errorList.append(idx)
      continue

    ratingCount = ratingList.select_one("em.product_num__fafe5")
    if ratingCount is None:
      print("data_search2 error -ratingcount is none")
      errorList.append(idx)
      continue

    data =[]
    data.append(productName.text.strip())
    data.append(productPrice.text.strip().replace("원","").replace(",",""))
    data.append(float(ratingStar.text.strip().replace("별점","")))
    data.append(int(ratingCount.text.strip().replace(",","").replace("(","").replace(")","").replace(".","").replace("만","")))
    
    # data = {
    #   "이름" : f"{productName.text.strip()}",
    #   "가격" : f"{productPrice.text.strip().replace("원","").replace(",","")}",
    #   "별점" : f"{float(ratingStar.text.strip().replace("별점",""))}",
    #   "리뷰" : f"{int(ratingCount.text.strip().replace(",","").replace("(","").replace(")","").replace(".","").replace("만",""))}"
    # }

    saveList.append(data)
    # print(f"이름 : {productName.text.strip()} , 가격 : {productPrice.text.strip()} , 별점 : {ratingStar.text.strip().replace("별점","")}, 리뷰 : {ratingCount.text.strip()}")
    

  # print(saveList)



option = Options()
option.add_argument('--headless')
option.add_argument('--window-size=1920,1080')
option.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

url = "https://www.naver.com"
# url = "https://search.shopping.naver.com/search/all?query=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

elem = browser.find_element(By.XPATH,'//*[@id="shortcutArea"]/ul/li[4]/a')
elem.click()

time.sleep(3)

last_tab = browser.window_handles[-1]
browser.switch_to.window(window_name=last_tab)

elem = browser.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')

elem.send_keys("무선 마우스")
elem.send_keys(Keys.ENTER)

time.sleep(2)

for i in range(5):

  proListData = []
  errorList = []
  
  prev_height = browser.execute_script('return document.body.scrollHeight')

  data1_length = 0
  data2_length = 0

  while True:

    soup = BeautifulSoup(browser.page_source,'lxml')  
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

    time.sleep(1)
    curr_height = browser.execute_script('return document.body.scrollHeight')
    print('이전 길이 : ', prev_height)
    if prev_height == curr_height:
      pageList = soup.select_one("#content > div.style_content__xWg5l > div.pagination_pagination__fsf34 > div")
      pageButton = pageList.select("a")
      break

    prev_height = curr_height
    
  productList = soup.select_one('#content > div.style_content__xWg5l > div.basicList_list_basis__uNBZx > div')
  productData1 = productList.select("div.adProduct_item__1zC9h")
  data1_length = int(len(productData1))
  
  productData2 = productList.select("div.product_item__MDtDF")
  data2_length = int(len(productData2))

  data_Search1(productData1, proListData, errorList)
  data_Search2(productData2, proListData, errorList)

  listLength = data1_length + data2_length
  print(listLength)
  with open(f"c1025/csvTest{i+1}.csv","w",encoding="utf-8", newline='') as csvFile:
    writer = csv.writer(csvFile)
    for row in proListData:
      writer.writerow(row)
    writer.writerow(f"{listLength}")
  

  elem = browser.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div[4]/div/a[{i+1}]')
  elem.click()
  time.sleep(3)



