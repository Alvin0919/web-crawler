import pandas as pd
import plotly.express as px

df = pd.read_csv('gdp-230408-185557.csv',delimiter=',')
print(df)

print('=====欄位資訊=====')
print(df.columns.values.tolist())

print('=====顯示前五筆=====')
print(df.head(5))

print('=====顯示每一筆資料=====')
for i,row in df.iterrows():
    print('i=',i)
    for v in row:
        print(v)
    print()

print('=====篩選=====')
q = "country=='Canada' or country=='Taiwan'"
df_Canada_Taiwan = df.query(q)
print(df_Canada_Taiwan)

fig = px.bar(df_Canada_Taiwan,x='year',y='pop',color='country',barmode='group')
fig.show()

country1 = input("請輸入第一個國家名稱：")
country2 = input("請輸入第二個國家名稱：")

# 篩選出相關的資料
df_country1 = df[df['country'] == country1]
df_country2 = df[df['country'] == country2]

# 取得兩個國家的資料列數
count1 = len(df_country1)
count2 = len(df_country2)
print(count1,count2)
# 設定長條圖的標籤和數值
labels = [country1, country2]
values = [count1, count2]

# 繪製長條圖
fig2=px.bar(labels, values)

# 顯示圖表
fig2.show()