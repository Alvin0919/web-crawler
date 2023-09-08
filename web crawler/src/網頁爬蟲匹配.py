import re
#模式pattern
#\d   數字0~9
#{n}  出現n次
#{n,m}出現n~m次
#^ 位置在文章開始
#$ 位置在文章結束
#* 出現零次以上
#+ 出現一次以上
# . 任意字(除了\r \n)
#\ 跳脫字元 可以用在特殊符號(標點符號)

#| 或

#r 代表字串是表達式文字，不做特殊解釋例如\n換行

##變數命名意義
#p模式
#s字串(文章)
#m代表是否匹配

##變數命名意義
#p模式
#s字串(文章)
#m代表是否匹配

s = '<html><head><title>網頁標題</title></head></html>'
#s = '<html><head><titleXXXXX>網頁標題</title></head></html>'
#s = '<html><head><titleAAAAAAAAAAAAAAAAA>網頁標題</title></head></html>'
p = r'<title>.+</title>'
print('-------匹配結果----------')
result = re.findall(p,s)
for x in result:
    print(x)

print('------------group群組--------------')
#將搜尋資料()分組，將來方便讀取當中任何一組
p = r'<title>(.+)</title>'
m = re.search(p,s)  # search()找找看，不一定有匹配
if m:
    print('找到匹配')
    #print(m.group())  #group() 沒有指定第幾組 第幾個()
    #print(m.group(0)) #group() 指定第0組 錯誤用法 從1算起
    print(m.group(1))
else:
    print('找不到匹配')