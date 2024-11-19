from selenium import webdriver
from selenium.webdriver.common.by import By as by
from selenium.webdriver.common.keys import Keys as keys
import time
import requests, random
from bs4 import BeautifulSoup

url = 'https://flight.naver.com'
browser = webdriver.Chrome()
browser.maximize_window() # 창 최대화 (전체화면)
browser.get(url)
# 출발지 선택
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[1]/b')
elem.click()
time.sleep(1)
# 김포 입력
elem = browser.find_element(by.CLASS_NAME, 'autocomplete_input__qbYlb')
elem.send_keys('김포')
time.sleep(1)
# 김포 공항 선택
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li[2]/a/b')
elem.click()
time.sleep(1)
# 도착지 선택
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[1]/button[2]')
elem.click()
time.sleep(1)
# 제주 입력
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[1]/div/input')
elem.send_keys('제주')
time.sleep(1)
# 제주 선택
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/section/ul/li/a/b')
elem.click()
time.sleep(1)
# 출발 날짜
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[1]')
elem.click()
time.sleep(1)
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[4]/button')
elem.click()
time.sleep(1)
# 도착 날짜
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[2]/button[2]')
elem.click()
time.sleep(1)
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[8]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[2]/td[7]/button')
elem.click()
time.sleep(1)
# 인원 선택
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[3]/button')
elem.click()
time.sleep(1)
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/div[4]/div/div/div[1]/div[1]/button[2]')
elem.click()
time.sleep(1)
# 항공권 검색
elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]')
# elem = browser.find_element(by.XPATH, '//*[@id="__next"]/div/main/div[2]/div/div/div[2]/button[1]/span')
elem.click()
elem.click()

time.sleep(15)

page_data = browser.find_element(by.XPATH,'//*[@id="__next"]/div/main/div[4]/div/div[2]')

soup = BeautifulSoup(browser.page_source,"lxml")
data = soup.select_one("#__next > div > main > div.domestic_flight_content__vYDHd > div > div.domestic_results__gp5WB")
print("*"*70)
print(data)




time.sleep(100)