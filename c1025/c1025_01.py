from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import requests
from bs4 import BeautifulSoup
import random
import pyautogui

url = "https://search.shopping.naver.com/search/all?adQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&origQuery=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&pagingIndex=1&pagingSize=40&productSet=total&query=%EB%AC%B4%EC%84%A0%20%EB%A7%88%EC%9A%B0%EC%8A%A4&sort=rel&timestamp=&viewType=list"
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(url)


soup = BeautifulSoup(browser.page_source,'lxml')

pageButton = soup.select_one("#content > div.style_content__xWg5l > div.pagination_pagination__fsf34 > div")

print(pageButton)
