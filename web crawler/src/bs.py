import requests
from bs4 import BeautifulSoup
r = requests.get(url='https://pokemondb.net/pokedex/national')
s = r.text ##文章
soup = BeautifulSoup(s,'html.parser')
print(soup.prettify()) #prettify() 排版內縮 容易閱讀

div = soup.find_all('div',class_='infocard')
print(div)
print('------------------------------------------------------------------------------------------------')

#all_span = div.find_all('span')  ##找出所有span子孫
#for span in all_span:
    #print(span)

print('------------------------------------------------------------------------------------------------')
#span = all_span[1]
#data_src = span['data-src']
#print(data_src)

print('------------------------------------------------------------------------------------------------')
print(soup.find('div',class_='infocard').find_all('span')[1]['data-src'])

print('------------------------------------------------------------------------------------------------')
span = soup.find('div',class_='infocard').find_all('span')[2]
small = span.find('small')
print(small.string)    #string 元素字串內容

print('------------------------------------------------------------------------------------------------')
span = soup.find('div',class_='infocard').find_all('span')[2]
a = span.find('a')
print(a.string)

print('------------------------------------------------------------------------------------------------')
small = soup.find('div',class_='infocard').find_all('small')[1]
a = small.find('a')
for x in small:
    print(x.string)

print('------------------------------------------------------------------------------------------------')
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