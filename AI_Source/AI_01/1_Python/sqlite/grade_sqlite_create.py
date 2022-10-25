import sqlite3

dbconn = sqlite3.connect('grade.db')
# 데이터베이스와 연결하기 위한 작업

dbcursor = dbconn.cursor()
# cursor라는 타입의 객체 생성

dbcursor.execute('''CREATE TABLE IF NOT EXISTS grade (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    kor INTEGER,
                    eng INTEGER,
                    math INTEGER,
                    sum INTEGER,
                    avg REAL,
                    grade TEXT
                )''')
# cursor 함수 실행문

# ------------------------ 데이터 출력 ------------------------

print('ID \t 이름 \t 국어 점수 \t 영어 점수 \t 수학 점수 \t 총점 \t 평균 \t 등급')

dbcursor.execute('SELECT * FROM grade')

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
          str(row[4]) + '\t' +
          str(row[5]) + '\t' +
          str(row[6]) + '\t' +
          str(row[7]) + '\t')

# ------------------------ commit ------------------------

dbcursor.execute('SELECT * FROM grade')

res = dbcursor.fetchone()
print(res)

res2 = dbcursor.fetchone()
print(res2)

dbconn.commit()
# insert 구문은 DML이므로 commit을 해줘야 함

dbcursor.close()
dbconn.close()