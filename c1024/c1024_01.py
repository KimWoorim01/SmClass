from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.support.ui import WebDriverWait as wdwait
from selenium.webdriver.support import expected_conditions as ec
import time
import requests, random
from bs4 import BeautifulSoup


url = "https://www.yanolja.com/"

browser = webdriver.Chrome()

browser.maximize_window()

browser.get(url)


browser.find_element(by.XPATH, '//*[@id="__next"]/div/div/header/section/a[2]/div/div').click()

time.sleep(2)

browser.find_element(by.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[2]/div[1]/button').click()

time.sleep(2)

browser.find_element(by.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[3]/td[4]').click()

time.sleep(2)

browser.find_element(by.XPATH,'/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[4]/td[3]').click()

time.sleep(2)

browser.find_element(by.XPATH,'/html/body/div[4]/div/div/section/section[4]/button').click()

time.sleep(2)

elem = browser.find_element(by.XPATH,'//*[@id="__next"]/div/main/div/div[1]/form/div/div[1]/div/input')

elem.click()
elem.send_keys("강릉 호텔")
elem.send_keys(keys.ENTER)

wdwait(browser,30).until(lambda x:x.find_element(by.XPATH,'//*[@id="__next"]/div/main/section/div[2]'))

soup = BeautifulSoup(browser.page_source,"lxml")

with open("c1024/yanolja.html","w",encoding="utf-8") as f:
  f.write(soup.prettify())

time.sleep(3)

soup = BeautifulSoup(browser.page_source,"lxml")


with open("c1024/yanolja.html","w",encoding="utf-8") as f:
  f.write(soup.prettify())

sectionList = soup.select_one("#__next > div > main > section > div.PlaceListBody_listContainer__2qFG1")
divList = sectionList.select("div.PlaceListItemText_container__fUIgA")
dataCount = 0
errorPoint = []
searchList = []
for idx, divData in enumerate(divList):


  imgData = divData.select_one("a")
  if imgData is None :
    errorPoint.append(idx)
    continue
  
  textData = divData.select_one("div.PlaceListItemText_contents__2GR73.place-content.PlaceListItemText_singlePrice__1aj9I")
  if textData is None:
    errorPoint.append(idx)
    continue

  title = textData.select_one("div.PlaceListTitle_container__qe7XH > strong")
  if title is None :
    errorPoint.append(idx)
    continue
  
  ratingStar = textData.select_one("span.PlaceListScore_rating__3Glxf")
  if ratingStar is None:
    errorPoint.append(idx)
    continue
  
  ratingInfo = textData.select_one("span.PlaceListScore_reviewInfo__3QSCU")
  if ratingInfo is None:
    errorPoint.append(idx)
    continue

  pricebox = textData.select_one("div.PlacePriceInfoV2_bottomInfo__2h62q")
  if pricebox is None:
    errorPoint.append(idx)
    continue

  price = pricebox.select_one("span.PlacePriceInfoV2_discountPrice__1PuwK")
  if price is None:
    errorPoint.append(idx)
    continue
  dataCount += 1
  searchData = {
    "NO" : dataCount,
    "호텔명" : title.text.strip(),
    "평점" : float(ratingStar.text.strip()),
    "리뷰" : int(ratingInfo.text.strip().replace(",","").replace("(","").replace(")","")),
    "가격" : int(price.text.strip().replace(",",""))
  }
  searchList.append(searchData)
  print(f"{dataCount}. {title.text.strip()} , 평점: {ratingStar.text.strip()}, 리뷰: {ratingInfo.text.strip()}, 가격: {price.text.strip()}")


searchList.sort(key=lambda x:x["가격"],reverse=True)
print(searchList[:5])
print(errorPoint)


# div.PlaceListTitle_container__qe7XH > strong


# with open("c1024/yanolja.html","r",encoding="utf-8") as f:
#   soup = BeautifulSoup(f,'lxml')


# prev_height = browser.execute_script("return document.body.scrollHeight")
# print(prev_height)

# while True:
#   browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
#   time.sleep(1)

#   curr_height = browser.execute_script("return document.body.scrollHeight")
#   if prev_height == curr_height:
#     print(curr_height)
#     break

# input("Enter 키 누르면 종료")





