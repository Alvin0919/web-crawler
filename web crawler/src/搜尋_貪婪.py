import re
# + 出現1次以上
# . 任意字(除了\r \n)

s = '<email>sx502502@gmail.com</emil><emil>amy@gmail.com</email>'
# 預設使用 貪婪模式 盡可能找出最大匹配範圍
p = r'<email>.+</email>'
print('--------findall-----------')
print('pattern:',p)
result = re.findall(p,s)
result = ('result type:',type(result))
print('len',len(result))
for x in result:
    print(x)

p = r'<email>(.+)</email>'
print('----------search group----------')
print('pattern:',p)
m = re.search(p,s) #searcj()找找看 不一定有匹配
if m:
    print('找到匹配')
    print(m.group(1))  #group()  指定第一組
else:
    print('找不到匹配')
