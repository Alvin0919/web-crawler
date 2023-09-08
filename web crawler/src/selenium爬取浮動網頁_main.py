import csv
import time
from bs4 import BeautifulSoup
from datetime import datetime
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

##下載瀏覽器
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

##最大化視窗
driver.maximize_window()

##擷取網頁
url = 'https://www.cnyes.com/twstock/2330/charts/technical-history'
driver.get(url)


##暫停(秒)等待網頁全部載入
time.sleep(5)

##找網頁元素按鈕
元素 = driver.find_element(
    By.XPATH,
       '//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/button'
)

#捲動網頁畫面至某個元素
js = 'arguments[0].scrollIntoView'  #js 執行碼 捲動畫面至某元素
driver.execute_script(js,元素)       #執行js 程式碼
# 點選 按鈕 元素
time.sleep(3)
元素.click()

#鍵盤打字 輸入 起始日
time.sleep(1)
元素 = driver.find_element(
    By.XPATH,
    '//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/div[2]/div[2]/div[1]/input'
)

time.sleep(2)
元素.clear()

##time.sleep(2)
元素.send_keys('20230101')

#找網頁按鈕 (套用)元素
time.sleep(1)
元素 = driver.find_element(
    By.XPATH,
    '//*[@id="tw-stock-tabs"]/section/section[2]/div[3]/div/div/section/div[1]/div/div[2]/div[3]/button[2]'
)
元素.click()

time.sleep(3)
s = driver.page_source
print(s)
print('=================')
time.sleep(3)
driver.quit()

##Beautiful Soup 整理爬取內容
soup = BeautifulSoup(s,'html.parser') #s是動態網頁內容

##整理出要擷取的部分
all_td = soup.find('tbody').find_all('td')
all_th = soup.find('thead').find_all('th')
for th in all_th:
    print(th.string.strip())
for td in all_td:
    print(td.string.strip())   ##strip 去除前後多於空白

##取得表格欄位標題
all_th = soup.find('thead').find_all('th')
headers = [th.string.strip() for th in all_th]

##取得表格內容
all_td = soup.find('tbody').find_all('td')
rows = []
for i in range(0, len(all_td), len(headers)):
    row = [td.string.strip() for td in all_td[i:i+len(headers)]]
    rows.append(row)

##讀取自己寫得函式 將目標資料夾的檔案移至備份資料夾
from src import fmove
O_path = 'C:/Users/user/Desktop/test'
n_path = 'C:/Users/user/Desktop/testbackup'
fmove.filemove(O_path,n_path)


##創建新的CSV檔案
filename = datetime.now().strftime('%Y%m%d_%H%M%S') + '_output.csv'
new_path = 'C:/Users/user/Desktop/test/' + filename
with open(new_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)






