import re
import pandas
from pandas_csv_main import 讀取csv
#txt = 'I like apple'
# x= txt.replace('apple','grape')
#print('txt = ',txt)
#print('x = ',x)

p = r'<tbody>.+<tbody>'
#p = r'<tbody>'
s = 讀取csv
# 尋找 \n 換行 取代成空字符 (即 刪除\n 換行)
s = s.replace('\n','')
#print(s)

result = re.findall(p,s)
print('type:',type(result))
print('lne',len(result))


