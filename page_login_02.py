import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pyperclip

# 웹드라이버 열기 (네이버 로그인 화면)
driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
driver.maximize_window()
delay = 15
driver.implicitly_wait(delay)

time.sleep(1)   # 1초 시간 지연

#아이디 삽입
id = driver.find_element("xpath", '//*[@id="id"]')
id.click() #클릭 이벤트 생성

pyperclip.copy('내 아이디') #클립보드에 id 복사
id.send_keys(Keys.CONTROL, 'v') #id input에 붙여넣기 
time.sleep(1)

# 비밀번호 삽입
password = driver.find_element("xpath", '//*[@id="pw"]')

pyperclip.copy('내 비밀번호') #클립보드에 id 복사
password.send_keys(Keys.CONTROL, 'v') #id input에 붙여넣기 
time.sleep(1)

# 로그인 버튼 누르기
loginbutton = driver.find_element("xpath", '//*[@id="log.login"]')
loginbutton.click()
time.sleep(1)

driver.get(url="https://www.naver.com/")