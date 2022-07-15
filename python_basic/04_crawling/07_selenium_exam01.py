from selenium import webdriver  #pip install selenium
import os,time

path = os.path.dirname(__file__) #현재파일의 디렉토리 경로를 가져온다
driver = webdriver.Chrome(path+'/driver/chromedriver')  #https://chromedriver.chromium.org/home에서 해당 크롬 버전에 맞게 다운로드 받아야함

driver.implicitly_wait(15)  #묵시적 대기. 제대로 뜰 때까지 최대 15초 까지는 기다려 주겠다(기본단위는 초) 
driver.get('https://google.co.kr') #겟방식으로 가져온다?
time.sleep(5) #5초정도를 쉬었다가
driver.quit() #종료