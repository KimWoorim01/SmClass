from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.support.ui import WebDriverWait as wdwait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.options import Options
import pyautogui as autogui
import time
import requests, random
from bs4 import BeautifulSoup


#노트북 검색후 1,2,3 페이지에서 
#만족도 95% 이상, 금액 150만원 이하, 평가수 100이상 검색

option = Options()
option.add_argument('--headless')
option.add_argument('--window-size=1920,1080')
option.add_argument("User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)")

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent/"

browser = webdriver.Chrome(options=option)
browser.maximize_window()
browser.get(url)

soup = BeautifulSoup(browser.page_source,"lxml")
data = soup.select_one("#detected_value")
print(data.text)

autogui.moveTo(50,100)
time.sleep(2)

autogui.scroll()

pre_height = browser.execute_script("return document.body.scrollHeight")

while True:
  autogui.scroll(-pre_height)
  time.sleep(2)
  curr_height = browser.execute_script("return document.body.scrollHeight")
  if pre_height == curr_height:
    break

  pre_height = curr_height

print("스크롤 내리기 끝")

autogui.moveTo(900,900)
autogui.click()

# for i in range(3):

#   url = "https://www.gmarket.co.kr/n/search?keyword=%EB%85%B8%ED%8A%B8%EB%B6%81"

#   browser = webdriver.Chrome()
#   browser.get(url)
#   time.sleep(3)
#   soup = BeautifulSoup(browser.page_source,"lxml")

#   with open("c1024/gmarket1.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())












