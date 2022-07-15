from selenium import webdriver  #셀레늄 라이브러리가 만들어진 목적은 테스트해보려고..
import os, time

path = os.path.dirname(__file__) #현재 폴더경로로 지정! __file__에는 현재 실행중인 파일의 경로가 들어있다.
driver = webdriver.Chrome(path+'/driver/chromedriver')
driver.implicitly_wait(15) #인터넷 상황에 따라서 이게 필요한 경우도 있고 필요하지 않은 경우도 있음

driver.fullscreen_window() #처음에 열릴 때 전체화면으로 열린다
time.sleep(3)
driver.minimize_window() #최소창크기로 변경
time.sleep(3)
driver.maximize_window()
time.sleep(3)

driver.set_window_rect(100,100,500,500)
time.sleep(3)
print(driver.get_window_rect()) #get은 가져오는거
time.sleep(3)
driver.set_window_position(0,0)
time.sleep(3)
driver.quit()
