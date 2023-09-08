# * 出現0次以上
# + 出現1次以上
# . 任意字(除了\r \n)

import re
s = 'XXXXXX<div>內容1</div><div>內容2</div>'
p = r'<div>.+</div>'
print(s)
print(p)
print('------貪婪--------')
#預設採用 貪婪模式 盡可能找出最大匹配
result = re.findall(p,s)
print('len:',len(result))
for x in result:
    print(x)
print()

#懶惰模式 找出最小匹配範圍
#懶惰模式 量詞 後面加上 ?
#  *?       出現零次以上
#  +?       出現一次以上
#  .?       任意字除了(\r \n)
p = r'<div>.+?</div>'
print(s)
print(p)
print('---------------懶惰--------------------')
result = re.findall(p,s)
print('len:',len(result))
for x in result:
    print(x)
print()

print('----------懶惰 search group----------------')
p = r'<div>(.+?)</div>'
m = re.search(p,s)
if m:
    print('找到匹配')
    print(m.group(1))
else:
    print('沒有找到匹配')

print('-------------懶惰 findall group------------------------')
p = r'<div>(.+?)</div>'
result = re.findall(p,s)
print('result type',type(result))
print('len:',len(result))
for x in result:
    print(x)
