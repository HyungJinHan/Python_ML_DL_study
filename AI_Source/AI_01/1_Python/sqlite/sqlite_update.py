import sqlite3

dbconn = sqlite3.connect('tel.db')
dbcursor = dbconn.cursor()
res = dbcursor.execute('SELECT * FROM tel ORDER BY id DESC')

name = input('수정할 이름을 입력하세요. => ')
flag = 0
for row in res:
    if row[1] == name:
        tel = input('전화번호를 입력하세요. => ')
        addr = input('주소를 입력하세요. => ')
        memo = input('메모할 것을 입력하세요. => ')
        dbcursor.execute('UPDATE tel SET tel =?, addr = ?, memo = ? WHERE name = ?',
                         (tel, addr, memo, name))
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
    print('수정이 완료되지 않았습니다.')
else:
    print('수정이 완료되었습니다.')

dbcursor.close()
dbconn.close()