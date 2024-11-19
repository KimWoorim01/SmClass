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

url = "https://new.land.naver.com/complexes/107929?ms=37.4592802,126.8930386,17&a=APT:PRE:ABYG:JGC&e=RETAIL"

browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)

autogui.moveTo(1270,610)
time.sleep(2)

autogui.moveTo(1470,500)



prev_height = browser.execute_script("return articleListArea.scrollHeight")
while True:
  autogui.scroll(-prev_height)
  time.sleep(2)
  curr_height = browser.execute_script("return articleListArea.scrollHeight")
  if prev_height == curr_height :
    break
  prev_height = curr_height
  print("높이 : ",prev_height)


soup = BeautifulSoup(browser.page_source,"lxml")

with open("c1024/naver.html","w",encoding="utf-8") as f:
  f.write(soup.prettify())


with open(f'c1024/naver.html', 'r', encoding='utf-8') as f:
  soup = BeautifulSoup(f, 'lxml')

  
data = soup.select_one("#complexOverviewList > div.list_contents > div.item_area > div.item_list.item_list--article")
data_list = data.select('div.item.false')
t_mm = [] # 매매
t_gs = [] # 전세
t_ws = [] # 월세
for i in data_list:
  point = i.select_one('.item_inner > .item_link')
  name = point.select_one('.item_title > .text').text.strip().replace('\n', '')
  t_type = point.select_one('.price_line > .type').text.strip().replace('\n', '')
  money_type = point.select_one('.price_line > .price > .slash')
  if money_type == None:
    money = point.select_one('.price_line > .price').text.strip().replace('\n', '').replace('\t', '')
    if money.find('억') != -1:
      money = money.replace('억', '')
      if money.find(',') != -1:
        money += '0000'
        money = money.replace(',', '')
      else:
        money += '00000000'
        money = money.strip()
  else:
    money = point.select_one('.price_line > .price').text.strip().replace('\n', '').replace('\t', '')
    # 억 뒤에 공 0개 추가
    money_1 = money[:money.find('/')].replace(' ', '').strip()
    if money_1.find('억') != -1:
      money_1 = money_1.replace('억', '')
      if money_1.find(',') != -1:
        money_1 += '0000'
        money_1 = money_1.replace(',', '')
      else:
        money_1 += '00000000'
        money_1 = money_1.strip()
    money_2 = money[money.find('/'):].replace('/', '').strip()
  money.find(' ')
  if money in '/':
    print(money)
    print(t_type)
  if t_type == '매매':
    t_mm.append({'이름':name, '타입':t_type, '가격':int(money.replace(' ', ''))})
  elif t_type == '전세':
    t_gs.append({'이름':name, '타입':t_type, '가격':int(money.replace(' ', ''))})
  elif t_type == '월세':
    t_ws.append({'이름':name, '타입':t_type, '보증금':int(money_1.replace(' ', '')), '월세':int(money_2.replace(' ', ''))})
print(t_mm)
print(t_gs)
print(t_ws)
