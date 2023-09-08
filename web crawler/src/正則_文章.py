import re
s = input('輸入文章:')
p = input('輸入表達式:')

print('======匹配結果======')

result = re.findall(p,s)
for x in result:
    print(x)