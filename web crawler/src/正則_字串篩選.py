import re

s = 'Tom 100 99 52000 90.5 80!5'
p = r'\d{1,3}'
result = re.findall(p,s)
for x in result:
    print(x)
