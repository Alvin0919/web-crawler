def 下載():
    r = requests.get(url = 'https://rate.bot.com.tw/xrt?Lang=zh-TW')
    s = r.text   ##文章(html網頁內容)
    return s

def 存檔(filename,s):     #參數 filename , s
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(s)



def 讀取檔案(filename):
    global s
    with open(filename,'r',encoding='utf-8') as f:
        s = f.read() #讀取所有內容字串
        #print(s)


def 下載存檔():
    s = 下載()
    filename = 'lab_14台銀匯率網頁.html'
    存檔(filename, s)


def 另存新檔_刪除換行():
    filename = 'lab_14台銀匯率網頁.html'
    s = 讀取檔案(filename)
    s = s.replace('\n','')  #尋找換行 換成空字串
    filename = 'lab_14台銀匯率網頁_另存.html'
    存檔(filename,s)




def 解析現金匯率():
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(s, 'html.parser')
    all_tr = soup.find_all('tr')
    tr=all_tr[2]
    all_td = tr.find_all('td')
    print(all_td[2].string)


def 所有現金金流():
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(s, 'html.parser')
    all_tr = soup.find_all('tr')
    tr=all_tr[2]
    for i in range(2,len(all_tr)):
        all_td=all_tr[i].find_all('td')
        print(all_td[0])
    for x in range(2,len(all_tr)):
        all_td=all_tr[x].find_all('td')
        print(all_td[1].string)
    for z in range(2, len(all_tr)):
        all_td = all_tr[z].find_all('td')
        print(all_td[2].string)

def 擷取網頁csv():
    all_df = pd.read_html('https://rate.bot.com.tw/xrt?Lang=zh-tw')
    print('type',type(all_df))
    df = all_df[0]
    df.to_csv('匯率.csv')
def 讀取csv():
    global df
    欄位名稱 = 1
    使用欄 = [1,3]
    欄名 =['幣別','現金買入']
    df = pd.read_csv('匯率.csv',header=欄位名稱,usecols=使用欄,names=欄名)
    print(df)