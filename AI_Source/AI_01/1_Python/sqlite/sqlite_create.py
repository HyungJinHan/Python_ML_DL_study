import sqlite3

dbconn = sqlite3.connect('tel.db')
# 데이터베이스와 연결하기 위한 작업

dbcursor = dbconn.cursor()
# cursor라는 타입의 객체 생성

dbcursor.execute('''CREATE TABLE IF NOT EXISTS TEL (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    tel TEXT,
                    addr TEXT,
                    input_time TEXT,
                    memo TEXT
                )''')
# cursor 함수 실행문

# ------------------------ 데이터 출력 ------------------------

print('No \t 성명 \t 전화번호 \t 전화번호 \t 주소 \t 메모 \t 입력 일자')

dbcursor.execute('SELECT * FROM tel ORDER BY id asc')

res = dbcursor.fetchall()
print(res)

for row in res:
    # dbcursor.execute('SELECT * FROM tel ORDER BY id asc')
    # for row in dbcursor.execute('SELECT * FROM tel'):
    #     print(row)
    print(str(row[0]) + '\t' +
          str(row[1]) + '\t' +
          str(row[2]) + '\t' +
          str(row[3]) + '\t' +
          str(row[5]) + '\t' +
          str(row[4]) + '\t')

# ------------------------ commit ------------------------

dbcursor.execute('SELECT * FROM tel ORDER BY id asc')

res = dbcursor.fetchone()
print(res)

res2 = dbcursor.fetchone()
print(res2)

dbconn.commit()
# insert 구문은 DML이므로 commit을 해줘야 함

dbcursor.close()
dbconn.close()