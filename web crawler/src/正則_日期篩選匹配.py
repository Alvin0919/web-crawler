#輸入regex表達式
import re
#模式pattern
#\d   數字0~9
#{n}  出現n次
#^ 位置在文章開始
#$ 位置在文章結束

##變數命名意義
#p模式
#s字串(文章)
#m代表是否匹配

p = r'^\d{4}-\d{1,2}-\d{1,2}$'
s = input('輸入西元日期(yyyy-MM-dd):')
m = re.search(p,s)
if m:
    print('匹配')
else:
    print('不匹配')