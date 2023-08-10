# 셀리니움_웹드라이버_네이버로그인.py
# pip install clipboard 
#자동화 테스트(스트레스 테스트)
#웹봇(자동화 코드)
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import clipboard
import time
#웹드라이버(webDriver.exe)실행파일로 크롬을 조정
#driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get('https://nid.naver.com/nidlogin.login')

# 네이버 메인화면에서 로그인 버튼 클릭
# driver.find_element_by_xpath('//*[@id="account"]/a').click()
# time.sleep(1)   # 1초 시간 지연

# 로그인 창에 아이디/비밀번호 입력
loginID = "park"
clipboard.copy(loginID)
#mac은 COMMAND, window는 CONTROL
#XPath는 계층으로 검색하는 문법 
driver.find_element(By.XPATH,'//*[@id="id"]').send_keys(Keys.CONTROL, 'v')

loginPW = "1234"
clipboard.copy(loginPW)
driver.find_element(By.XPATH,'//*[@id="pw"]').send_keys(Keys.CONTROL, 'v')
time.sleep(1)

# 로그인 버튼 클릭
driver.find_element(By.XPATH,'//*[@id="log.login"]').click()

while True:
    pass 