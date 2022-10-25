import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()
res = dbcursor.execute('SELECT * FROM tel ORDER BY id DESC')

name = input('삭제할 이름을 입력하세요. => ')
flag = 0
for row in res:
    if row[1] == name:
        dbcursor.execute('DELETE FROM tel WHERE name = ?', (name, ))
        dbconn.commit()
        flag = 1

print('No \t 성명 \t 전화번호 \t 전화번호 \t 주소 \t 메모 \t 입력 일자')

dbcursor.execute('SELECT * FROM tel ORDER BY id asc')

res = dbcursor.fetchall()

for row in res:
    print(str(row[0]) + '\t' +
          str(row[1]) + '\t' +
          str(row[2]) + '\t' +
          str(row[3]) + '\t' +
          str(row[5]) + '\t' +
          str(row[4]) + '\t')

if flag == 0:
    print('삭제가 완료되지 않았습니다.')
else:
    print('삭제가 완료되었습니다.')

dbcursor.close()
dbconn.close()