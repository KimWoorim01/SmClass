import os
import time
import requests
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

url = "http://www.naver.com"

browser =webdriver.Chrome()
browser.get(url)

elem = browser.find_element(By.CLASS_NAME, "MyView-module__link_login___HpHMW")

elem.click()
time.sleep(random.randint(2,5))

# elem = browser.find_element(By.ID,"id")
# elem.send_keys("yop133")
# time.sleep(random.randint(2,5))

# elem = browser.find_element(By.ID,"pw")
# elem.send_keys("yo991jvcxz")
# time.sleep(random.randint(2,5))

#자바 스크립트 호출방법
id = "'yop133'"
pw = "'tesxcvzxcv'"
input_js = f'document.getElementById("id").value ={id};\
  document.getElementById("pw").value ={pw};'
browser.execute_script(input_js)
time.sleep(random.randint(2,5))



elem = browser.find_element(By.ID,"log.login")
elem.click()