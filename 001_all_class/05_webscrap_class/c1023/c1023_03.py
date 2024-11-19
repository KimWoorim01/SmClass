import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup



# Chrome() 안에 chromedriver.exe 위치 지점을 입력해줘야 함(원래는)
# root에 파일 저장되어 있으면 입력 안해도 된다.

browser = webdriver.Chrome()
browser.get("https://naver.com")

# html 위치 찾기
search_input = "#query"
# elem = browser.find_element(By.CLASS_NAME,"MyView-module__link_login___HpHMW")

# elem.click()
# elem = browser.find_element(By.ID, "pW")


elem = browser.find_element(By.ID, "query")
elem.send_keys("네이버 영화")
elem.send_keys(Keys.ENTER)
# elem.click()
time.sleep(10)

# 새창 이동
browser.switch_to.window(browser.window_handles[1])

time.sleep(10)

# browser.back()
# browser.forward()


