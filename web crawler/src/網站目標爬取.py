import requests
from bs4 import BeautifulSoup
r = requests.get(url='https://pokemondb.net/pokedex/national')
s = r.text ##文章
soup = BeautifulSoup(s,'html.parser')
print(soup.prettify()) #prettify() 排版內縮 容易閱讀

div_all = soup.find_all('div',class_='infocard')
for div in div_all:
    print(div)
    span = div.find_all('span')[2]
    small = span.find_all('small')
    a = span.find_all('a')            #a = small.find_all('a')
    data_src =span.find_all('data-src')
    for z in small:
        print(z.string) #string 元素字串內容
    for e in a:
        print(e.string)
    for pic in data_src:
        print(pic.string)