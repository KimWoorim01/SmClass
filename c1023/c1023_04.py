import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup

browser = webdriver.Chrome()
browser.get("http://daum.net")

elem = browser.find_element(By.ID,"q")
elem.send_keys("주식정보")
elem.send_keys(Keys.ENTER)

browser.get("http://naver.com")
elem = browser.find_element(By.CLASS_NAME, "search_input")
elem.send_keys("주식정보")
elem.send_keys(Keys.ENTER)


time.sleep(100)
















# import time
# import random

# a= [0]*100
# for i in range(100):
#   a[i] = i
# b= [i+1 for i in range(100)]
# # print(a)
# # print(b)

# for i in b :
#   print(i)
#   time.sleep(random.uniform(1,3))