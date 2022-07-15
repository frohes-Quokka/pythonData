from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time,os

path = os.path.dirname(__file__)
driver = webdriver.Chrome(path+'/driver/chromedriver')
driver.get('http://www.naver.com')
query = driver.find_element(By.ID, 'query')  #웹사이트창에서 id='query'에 해당하는 요소를 가져온다 
query.clear()  #입력창에 입력되어있다면 깨끗하게 정리!
query.send_keys('여름바다')
time.sleep(2)
query.send_keys(Keys.ENTER)
time.sleep(2)
blogitem = driver.find_element(By.CLASS_NAME, 'keyword_item')
blogitem.click()
time.sleep(2)
print(driver.page_source)

#blogitem.send_keys(Keys.ENTER)