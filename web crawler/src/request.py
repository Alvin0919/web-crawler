import requests
import re

r = requests.get(url='https://pokemondb.net/pokedex/national')
print('狀態碼',r.status_code)
if r.status_code == 200:
    print('下載成功') # 200 代表成功
    print(r.text) #網頁內容
    print('--------------------------')

    # 瀏覽器畫面中的圖片 > 右鍵 > 檢測(檢查)

s = r.text
p = r'<span class="img-fixed.+?>'
result = re.findall(p,s)
print('result len:',len(result))
for x in result:
    print(x)
else:
    print('下載失敗')
