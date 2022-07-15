from selenium import webdriver
import os, time

path = os.path.dirname(__file__) #현재 폴더경로로 지정! __file__에는 현재 실행중인 파일의 경로가 들어있다.
driver = webdriver.Chrome(path+'/driver/chromedriver')
driver.implicitly_wait(15)

driver.get('https://life-of-wanderer.tistory.com/')
time.sleep(3)
driver.get('https://www.youtube.com')
time.sleep(3)
driver.get('https://www.naver.com')
time.sleep(3)

driver.back() #뒤로가기 버튼 누르기
time.sleep(3)
driver.back() #한번 더 뒤로가기
time.sleep(3)

driver.forward()
time.sleep(3)
driver.forward()
time.sleep(3)

driver.quit()

