import re
s = 'XXXXXXXX yicheng.980919@gmail.com XXXXXXXXX'
p = r'(\S+?)\.(\S+?)\@(\S+)'

m = re.search(p,s)
if m:
    print('找到匹配')
    print(m.group(1))
    print(m.group(2))
    print(m.group(3))
else:
    print('找不到匹配')