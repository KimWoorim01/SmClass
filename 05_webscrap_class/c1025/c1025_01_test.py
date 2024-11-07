





def naver_sreach():
  url = 'https://www.naver.com'
  wep = webdriver.Chrome()
  wep.maximize_window()
  wep.get(url)
  time.sleep(2)
  elem = wep.find_element(By.XPATH, '//*[@id="query"]')
  elem.click()
  time.sleep(2)
  elem.send_keys('네이버 쇼핑')
  time.sleep(1)
  elem.send_keys(Keys.ENTER)
  time.sleep(3)
  elem = wep.find_element(By.XPATH, '//*[@id="main_pack"]/section[1]/div/div/div[1]/div/div[2]/a')
  elem.click()
  time.sleep(3)
  # 다음텝 페이지 전환
  next_page = wep.window_handles[1]
  wep.switch_to.window(window_name=next_page)
  elem = wep.find_element(By.XPATH, '//*[@id="gnb-gnb"]/div[2]/div/div[2]/div/div[2]/form/div[1]/div/input')
  elem.click()
  elem.send_keys('무선 마우스')
  time.sleep(1)
  elem.send_keys(Keys.ENTER)
  time.sleep(3)
  for i in range(5):
    prev_height = wep.execute_script('return document.body.scrollHeight')
    while True:
      # 스크롤 내림
      wep.execute_script('window.scrollTo(0, document.body.scrollHeight)')
      # 화면 로딩 대기
      time.sleep(1)
      # 페이지가 로딩되면서 길어진 길이를 다시 가져옴
      curr_height = wep.execute_script('return document.body.scrollHeight')
      print('이전 길이 : ', prev_height)
      # 이전 최대 높이와 현제 최대 높이 비교
      if prev_height == curr_height:
        break
      prev_height = curr_height
    # 2번 클릭
    elem = wep.find_element(By.XPATH, f'//*[@id="content"]/div[1]/div[4]/div/a[{i+1}]')
    elem.click()
    time.sleep(3)
    soup = BeautifulSoup(wep.page_source, 'lxml')
    with open(f'20241025/naver_market_{i+1}.html', 'w', encoding='utf-8') as f:
      f.write(soup.prettify())