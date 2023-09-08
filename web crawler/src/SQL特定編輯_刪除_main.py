import sqlite3
def connetion():
    global con, c ##宣告函數內使用那些外面的全域變數
    con = sqlite3.connect('my.db')
    c = con.cursor()
    print('連線成功')


def closedb():
    con.close()
    print('關閉資料庫成功')


def create():
    global s
    s = '''
    CREATE TABLE exchange(
    id INTEGER,
    date TEXT,
    currency TEXT,
    cashin  REAL,
    cashout REAl,
    PRIMARY KEY("id")
    )
    '''
    try:
        print(s)
        c.execute(s)
        con.commit()
        print('exchange 資料表建立完成')
    except sqlite3.OperationalError as e:
        print('SQL語句執行錯誤')
        print(e)


def addsource(d):
    try:
        print(d)
        c.execute(d)
        con.commit()
        print('新增完成')
    except sqlite3.OperationalError as e:
        print('SQL語句執行錯誤')
        print(e)
    except sqlite3.IntegrityError as e:
        print('主鍵值錯誤 必須是唯一')
        print('請檢查exchange ID是否是唯一')
        print(e)


def selectda():
    s = '''
    SELECT*FROM exchange 
    '''
    try:
        print(s)
        result = c.execute(s)
        con.commit()
        print('查詢完成')
        for i in result:
            print(i)
    except sqlite3.OperationalError as e:
        print('SQL語句執行錯誤')
        print(e)


def lSELECT():
    s = '''SELECT*FROM exchange 
     '''
    try:
        print(s)
        result = c.fetchall()
        print('長度',len(result))
        for 筆 in result:
            print(筆)
    except sqlite3.OperationalError as e:
        print('SQL語句執行錯誤')
        print(e)
def searchall():
    print('查詢所有資料長度')
    s = '''SELECT * FROM exchange
    '''
    try:
        print(s)
        c.execute(s)
        con.commit()
        print('查詢完成')
        result = c.fetchall()
        print('長度',len(result))
        for 筆 in result:
            print(筆)
    except sqlite3.OperationalError as e:
        print('SQL語句執行錯誤')
        print(e)

def searchsing(編號):
    s = f'SELECT * FROM exchange WHERE id={編號}'
    print('查詢單筆資料')
    try:
        print(s)
        result = c.execute(s)
        con.commit()
        print('查詢完成')
        result = c.fetchall()
        print('長度',len(result))
        if len(result) == 0:
            print('查無資料')
            return
        for 筆 in result:
            print(筆)
    except sqlite3.OperationalError as e:
        print('SQL語句執行錯誤')
        print(e)


def deletesig(編號):
    s = f'DELETE  FROM exchange WHERE id = {編號}'
    sd = ''' SELECT*FROM exchange '''
    print('刪除單筆資料')
    try:
        print(s)
        result = c.execute(s)
        con.commit()
        print('刪除完成')
        print(sd)
        c.execute(sd)
        con.commit()
        result = c.fetchall()
        for 筆 in result:
            print(筆)
    except sqlite3.OperationalError as e:
        print('SQL語句執行錯誤')
        print(e)

def deleteall():
    s = '''DELETE  FROM exchange'''
    sd = ''' SELECT*FROM exchange '''
    print('刪除所有資料')
    try:
        print(s)
        result = c.execute(s)
        con.commit()
        print('刪除完成')
        print(sd)
    except sqlite3.OperationalError as e:
        print('SQL語句執行錯誤')
        print(e)

def continuetOdelete():
        # 檢查是否還有需要刪除的項目
        try:
            ans = input('是否還有需要刪除的項目？(Y/N): ')
            if ans.upper() == 'Y':
                # 繼續刪除
                j = input(('請輸入編號進行刪除'))
                deletesig(j)
                # 再次詢問是否需要繼續刪除
                ans = input('是否還有需要刪除的項目？(Y/N): ')
                while ans.upper() == 'Y':
                    deletesig(j)
                    ans = input('是否還有需要刪除的項目？(Y/N): ')
            else:
                # 結束刪除
                print('刪除作業結束')

        except sqlite3.OperationalError as e:
            print('SQL語句執行錯誤')
            print(e)


##主流成 全域變數
con = None
c = None
connetion()
#create()
addsource(d='''INSERT INTO exchange VALUES(5,'USD','AA',32,4698.3)''')
addsource(d='''INSERT INTO exchange VALUES(10,'bb','BB',32.15,4698.3)''')
selectda()
searchall()
print('----------------------')
i = input(('請輸入編號進行查詢'))
searchsing(i)
j = input(('請輸入編號進行刪除'))
deletesig(j)
#deleteall()
continuetOdelete()
closedb()
