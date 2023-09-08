import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#開啟Chrome

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#最大化視窗

driver.maximize_window()

#擷取網頁

url = 'https://www.cnyes.com/twstock/2330'
driver.get(url)

#暫停(秒)等待網頁全部載入

time.sleep(5)

s=driver.page_source
print(s)
print('=============')

time.sleep(3)
driver.quit()

