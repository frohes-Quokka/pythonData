# from bs4 import BeautifulSoup
# import urllib.request
# import requests


# starbucks = requests.get('https://www.starbucks.co.kr/store/store_map.do')
# print(starbucks.text)
# soup = BeautifulSoup(starbucks.text, 'lxml')
# item = soup.select_one('li.quickResultLstCon')
# print(item)


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,os

path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')
driver.get('https://www.starbucks.co.kr/store/store_map.do')
time.sleep(10)  #이게 제대로 안들어가면 데이터를 못받아 올수도 있음
soup = BeautifulSoup(driver.page_source, 'lxml')
result = soup.select('ul.quickSearchResultBox li.quickResultLstCon')
# location = driver.find_element(By.CLASS_NAME, 'quickResultLstCon') 
for item in result:
    print(item.text)

