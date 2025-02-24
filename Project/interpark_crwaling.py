# 프로그램으로 배포
# 프로그램 실행하면 인터파크 공연 정보 크롤링
# 수집 끝났으면 정리된 우리 캘린터 파일 실행

# 라이브러리 모음
from selenium import webdriver as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import csv
import os
import requests
import glob

# 인터파크 접속
url_naver_image = "https://tickets.interpark.com/contents/genre/concert"
driver = wb.Chrome()
driver.get(url_naver_image)


send_text = input("검색어를 입력하세요 :")

if not os.path.isdir(send_text):
    os.mkdir(send_text)
else:
    print("폴더가 존재합니다.")

show_whole = driver.find_element(By.CLASS_NAME, "SubCategory_btnCategory__i_55b")
show_whole.click()
time.sleep(3)



driver.close()