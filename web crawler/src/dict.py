import pandas as pd
import plotly.express as px
#建立字典資料
data = dict(月份=['Jan','Feb','Mar'],台積電=[1,2,3])
print(data)

#利用pandas建立資料表dataFrame
df = pd.DataFrame(data)
print(df)

#melt 預處理
df2 = df.melt(id_vars='月份',var_name='個股名稱',value_name='成交張數')
print(df2)

#製作長條圖
fig = px.bar(df2,x='月份',y='成交張數',color='個股名稱'
             )
#fig.show()

data2 = dict(場次=['第一場','第二場','第三場'], A隊 =[1,2,3], B隊 =[1,2,3] )
df3 = pd.DataFrame(data2)
df4 = df3.melt(id_vars='場次',var_name='隊名',value_name='得分')
print(df4)
fig = px.bar(df4,x='場次',y='得分',color='隊名',barmode='group'
             )
fig.show()