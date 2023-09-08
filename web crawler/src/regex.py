#載入regex表達式
import re
#模式pattern
#\d   數字0~9
#{n}  出現n次
##變數命名意義
#p模式
#s字串(文章)
#m代表是否匹配

p = r'\d{4}' #r代表字串中是表達式的文字，不做特殊解釋，例如\n 換行
s = input('輸入西元年(四位):')
m = re.search(p,s) #m 代表是否匹配
if m:
    print('匹配，文章中找到符合4個數字')
else:
    print('不匹配，文章中找不到符合4個數字')



