# 웹크롤링 시작
# webdriver selenium 으로 네이버 오픈해보기


from selenium import webdriver
driver = webdriver.Chrome() # 같은 위치라서 () / 다른 위치면 (" 주소 ")로 입력하기
url = 'https://www.naver.com'
driver.get(url)