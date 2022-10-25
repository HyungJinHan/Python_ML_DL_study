import pymysql

dbconn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='bbs',
    charset='utf8'
)

dbcursor = dbconn.cursor()

dbcursor.execute('''CREATE TABLE IF NOT EXISTS naver_mysql (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    title TEXT,
                    bloggername TEXT,
                    link TEXT,
                    bloggerlink TEXT,
                    postdate TEXT
                )''')

dbcursor.execute('SELECT * FROM naver_mysql')

res = dbcursor.fetchall()
print(res)