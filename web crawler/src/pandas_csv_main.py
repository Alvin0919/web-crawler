import matplotlib
import pandas as pd
import lxml
import plotly.express as px
import matplotlib.pyplot as plt
import csv
import matplotlib.font_manager as fm
#font_path = 'C:\Windows\Fonts\kaiu'
#prop = fm.FontProperties(fname=font_path)
#plt.rcParams['font.family'] = prop.get_name()
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
def 篩選有交易的貨幣():
    global df
    條件 = '現金買入 != "-" '
    df = df.query
    print(df)

def 查詢幣別():
    import csv
    global df
    with open('匯率.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        search_terms = input('請輸入所有要查詢的關鍵字，以逗號分隔：').split('，')
        for df in reader:
            matches = []
            for cell in df[1:4]:                          ##從第一欄開始查詢到第三欄
                for search_term in search_terms:
                    if search_term in cell:
                        matches.append(cell)
            if matches:
                print(df[1:4])


def 長條圖1():
    x_data = []
    y_data = []
    with open('匯率.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        print('美金')
        print('港幣')
        print('歐元')
        search_terms = input('請選擇幣別，以逗號分隔：').split('，')
        for df in reader:
            matches = []
            for cell in df[1:4]:
                for search_term in search_terms:
                    if search_term in cell:
                        matches.append(cell)
            if matches:
                x_data.append(df[0])
                y_data.append(float(df[3]))

    fig = px.bar(x=x_data, y=y_data)
    fig.update_layout(
        xaxis_title='幣別',
        yaxis_title='匯率',
        title='幣種: ' + ', '.join(search_terms)
    )
    fig.show()



##主流程
擷取網頁csv()
讀取csv()
篩選有交易的貨幣()
查詢幣別()
#長條圖1()
