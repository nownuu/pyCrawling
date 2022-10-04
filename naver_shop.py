# from tkinter import BROWSE
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome();
driver.get("https://shopping.naver.com/home") 

# 스크롤 전 높이 = 0
fo_h = driver.execute_script("return window.scrollY")

# 스크롤 (무한)
while True:
    driver.find_element_by_css_selector("body").send_keys(Keys.END)
    time.sleep(2)

    af_h = driver.execute_script("return window.scrollY")

    if fo_h == af_h:
        break
    
    fo_h = af_h


items = driver.find_element_by_css_selector('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[5]/li/div/div[2]')

for item in items:
    name = item.find_element_by_css_selector('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[5]/li/div/div[2]/div[1]')
    try:
        price = item.find_element_by_css_selector('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[5]/li/div/div[2]/div[2]/strong/span[1]/span')
    except:
        price = "판매 중단"

    link = item.find_element_by_css_selector('//*[@id="__next"]/div/div[2]/div[2]/div[3]/div[1]/ul/div/div[5]/li')
    print(name, price, link)


