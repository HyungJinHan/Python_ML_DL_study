import pymysql

dbconn = pymysql.connect(
    host='localhost',
    user='root',
    password='123456',
    db='bbs',
    charset='utf8'
)
# 데이터베이스와 연결하기 위한 작업

dbcursor = dbconn.cursor()
# cursor라는 타입의 객체 생성

dbcursor.execute('''CREATE TABLE IF NOT EXISTS grade_mysql (
                    id VARCHAR(20) PRIMARY KEY,
                    name VARCHAR(20),
                    kor INT,
                    eng INT,
                    math INT,
                    sum INT,
                    avg FLOAT,
                    grade VARCHAR(20)
                )''')
# cursor 함수 실행문

# ------------------------ 데이터 출력 ------------------------

print('ID \t 이름 \t 국어 점수 \t 영어 점수 \t 수학 점수 \t 총점 \t 평균 \t 등급')

dbcursor.execute('SELECT * FROM grade_mysql')

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

dbcursor.execute('SELECT * FROM grade_mysql')

res = dbcursor.fetchone()
print(res)

res2 = dbcursor.fetchone()
print(res2)

dbcursor.close()
dbconn.close()