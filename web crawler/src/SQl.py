import sqlite3
#連接聯繫資料庫
#檔案諾不存在會自動建立
con = sqlite3.connect('my.db') #my.db是資料庫檔案名稱

#透過連線取得cursor 游標
c = con.cursor()

#建立employee 員工資料表 使用CREATE TABLE
#SQlite 資料類型
#整數 INTEGER
#浮點數 REAL
#字串or日期 TEXT
#主鍵 PRIMARY KEY
#不能是NULL空直，必填
#值不能重複
#使用三個引號 字串可多行

s = '''
CREATE TABLE employee(
    id INTEGER,
    firstname TEXT,
    lastname TEXT,
    birthday TEXT,
    salary INTEGER,
    PRIMARY KEY("id")
)
'''
#透過CURSOR 游標 執行SQL語句

try:
    print(s)
    c.execute(s) #執行SQL語句
    con.commit() #提交執行SQL語句
    print("employee資料表建立完成")
except sqlite3.OperationalError as e:
    print('SQL語句執行錯誤')
    print(e)


##新增資料 INSERT INTO
##注意 日期格式 'yyyy-mm-dd'
## s ='''
##INSERT INTO employee VALUES(1,'aa','AA','1991-01-01,50000)
###'''

s = '''INSERT INTO employee VALUES(2,'bb','BB','1998-09-19',60000)
'''
#透過CURSOR 游標 執行SQL語句

try:
    print(s)
    c.execute(s) #執行SQL語句
    con.commit() #提交執行SQL語句
    print("新增 完成")
except sqlite3.OperationalError as e:
    print('SQL語句執行錯誤')
    print(e)
except sqlite3.IntegrityError as e:
    print('主鍵值錯誤 必須是唯一')
    print('請檢查員工編號ID是否是唯一')
    print(e)

# 查詢資料 SELECT
#* 代表每一欄都要
s = '''
SELECT*FROM employee
'''
try:
    print(s)
    結果 = c.execute(s)
    con.commit()
    print('查詢完成')
    for 筆 in 結果:
        print('筆')
except sqlite3.OperationalError as e:
    print('SQL語句執行錯誤')
    print(e)

con.close()
