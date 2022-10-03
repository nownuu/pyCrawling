import time 
from selenium import webdriver 
from selenium.webdriver.common.by import By


# 크롬 웹드라이버를 이용하여 크롬을 실행
driver = webdriver.Chrome()
driver.get("https://finance.naver.com/sise/") 
driver.maximize_window()
delay = 15
driver.implicitly_wait(delay)

time.sleep(2)

# html elemnt id가 stock_items 찾기
inputElement = driver.find_element(By.ID, 'stock_items')
time.sleep(2)

#종목 검색창에 삼성전자을 입력 
inputElement.send_keys("삼성전자") 
time.sleep(2)

# 검색내용 -> 서버측으로 이동
inputElement.submit()
time.sleep(2)

# 삼성전자 두 리스트 중 한개를 클릭
stockbutton = driver.find_element("xpath", '//*[@id="content"]/div[4]/table/tbody/tr[1]/td[1]/a')
stockbutton.click()
time.sleep(2)

# 종목분석 클릭 
continue_link = driver.find_element(By.PARTIAL_LINK_TEXT, '종목분석')
time.sleep(2)
continue_link.click() 
time.sleep(10)

driver.quit()