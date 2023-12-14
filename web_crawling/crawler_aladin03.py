


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# 엑셀 처리 모듈 임포트
# pip install xlsxwriter
import xlsxwriter

# user-agent 정보를 변환해 주는 모듈 임포트
# 특정 브라우저로 크롤링을 진행할 때 차단되는 것을 방지
# pip install fake_useragent
from fake_useragent import UserAgent

# 이미지를 바이트 변환 처리 모듈
from io import BytesIO

# 요청 헤더 정보를 꺼내올 수 있는 모듈
import urllib.request as req

d = datetime.today()

file_path = f'C:/test/알라딘 베스트셀러 1~400위_{d.year}_{d.month}_{d.day}.xlsx'

# User Agent 정보 변환 ( 필수는 아닙니다. )
opener = req.build_opener() # 헤더 정보를 초기화
opener.addheaders=['User-agent', UserAgent().chrome]
req.install_opener(opener) # 새로운 헤더 정보를 삽입

# 엑셀 처리 선언
# Workbook 객체를 생성해서 엑셀 파일 하나를 생성 (매개값으로 저장될 경로를 지정 )
workbook = xlsxwriter.workbook(file_path)

# 워크 시트 생성
worksheet = workbook.add_worksheet()

# 크롬 드라이버 구동
options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

# 브라우저 안뜨게 하기 
options.add_argument('--headless')