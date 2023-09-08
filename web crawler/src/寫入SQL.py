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
    CREATE TABLE employee(
    id INTEGER,
    firstname TEXT,
    lastname TEXT,
    birthday TEXT,
    salary INTEGER,
    PRIMARY KEY("id")
    )
    '''
    try:
        print(s)
        c.execute(s)
        con.commit()
        print('employee資料表建立完成')
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
        print('請檢查員工標號ID是否是唯一')
        print(e)


def selectda():
    s = '''
    SELECT*FROM employee
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
    s = '''SELECT*FROM employee
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

##主流成 全域變數
con = None
c = None
connetion()
create()
addsource(d='''INSERT INTO employee VALUES(100,'aa','AA','1998-09-19',60000)
''')
addsource(d='''INSERT INTO employee VALUES(200,'bb','BB','1998-09-19',60000)
''')
selectda()
closedb()