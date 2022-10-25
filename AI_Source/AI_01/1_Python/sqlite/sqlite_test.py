import sqlite3
import time

dbconn = sqlite3.connect('tel.db')
# 데이터베이스와 연결하기 위한 작업

dbcursor = dbconn.cursor()
# cursor라는 타입의 객체 생성

# ------------------------ 테이블 생성 ------------------------

dbcursor.execute('''CREATE TABLE IF NOT EXISTS TEL (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    tel TEXT,
                    addr TEXT,
                    input_time TEXT,
                    memo TEXT
                )''')
# cursor 함수 실행문

# ------------------------ 값 입력 ------------------------

name = input('이름을 입력하세요. => ')
tel = input('전화번호를 입력하세요. => ')
addr = input('주소를 입력하세요. => ')
memo = input('메모할 것을 입력하세요. => ')
input_time = str(time.asctime(time.localtime(time.time())))

# ------------------------ 값 DB에 넣기 ------------------------

# print('INSERT INTO tel.db (name, tel, addr, input_time, memo)) \
#       VALUES ('"+name+"', '"+tel+"', '"+addr+"', '"+input_time+"', '"+memo+"')')

# dbcursor.execute('INSERT INTO tel (name, tel, addr, input_time, memo) \
#                 VALUES ('"+name+"', '"+tel+"', '"+addr+"', '"+input_time+"', '"+memo+"')')

# dbcursor.execute('INSERT INTO tel (name, tel, addr, input_time, memo) VALUES (?, ?, ?, ?, ?)',
#                  (name, tel, addr, input_time, memo))
# 튜플 형으로 칼럼에 추가하겠다는 의미

# dbcursor.execute('INSERT INTO tel (name, tel, addr, input_time, memo) VALUES'
#                  '(:name, :tel, :addr, :input_time, :memo)',
#                  {'name': name, 'tel': tel, 'addr': addr, 'input_time': input_time, 'memo': memo}
#                  )
# 딕셔너리 형으로 칼럼에 추가하겠다는 의미

# ------------------------ 한 번에 여러 데이터 넣기 ------------------------

data = [
        ('한형진', '01000000000', '서울',
         str(time.asctime(time.localtime(time.time()))), '팀장입니다.'),
        ('전우진', '01011111111', '대전',
         str(time.asctime(time.localtime(time.time()))), '팀원입니다.'),
        ('김성환', '01022222222', '대구',
         str(time.asctime(time.localtime(time.time()))), '팀원입니다.'),
        ('김건', '01033333333', '부산',
         str(time.asctime(time.localtime(time.time()))), '팀원입니다.'),
        ]

sql = 'INSERT INTO tel (name, tel, addr, input_time, memo) VALUES (?, ?, ?, ?, ?)'
# sql = 'INSERT INTO TEL VALUES (null, ?, ?, ?, ?)'

dbcursor.executemany(sql, data)

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

    # 1	한형진	01000000000	건영아파트	이것은 테스트입니다.	Mon Sep 19 16:40:10 2022
    # 2	한형주	01011111111	건영아파트	이거슨 동생	Mon Sep 19 16:47:54 2022
    # 3	한형진	01000000000	서울	팀장입니다.	Mon Sep 19 17:01:51 2022
    # 4	전우진	01011111111	대전	팀원입니다.	Mon Sep 19 17:01:51 2022
    # 5	김성환	01022222222	대구	팀원입니다.	Mon Sep 19 17:01:51 2022
    # 6	김건	    01033333333	부산	팀원입니다.	Mon Sep 19 17:01:51 2022
    # 7	한형진	01000000000	서울	팀장입니다.	Mon Sep 19 17:28:30 2022
    # 8	전우진	01011111111	대전	팀원입니다.	Mon Sep 19 17:28:30 2022
    # 9	김성환	01022222222	대구	팀원입니다.	Mon Sep 19 17:28:30 2022
    # 10김건	    01033333333	부산	팀원입니다.	Mon Sep 19 17:28:30 2022

# ------------------------ commit ------------------------

dbcursor.execute('SELECT * FROM tel ORDER BY id asc')

res = dbcursor.fetchone()
print(res)

res2 = dbcursor.fetchone()
print(res2)

# (1, '한형진', '01000000000', '건영아파트', 'Mon Sep 19 16:40:10 2022', '이것은 테스트입니다.')
# (2, '한형주', '01011111111', '건영아파트', 'Mon Sep 19 16:47:54 2022', '이거슨 동생')

dbconn.commit()
# insert 구문은 DML이므로 commit을 해줘야 함

# for row in dbcursor.execute('SELECT * FROM tel'):
#     print(row)

dbcursor.close()
dbconn.close()

# 이름을 입력하세요. => 한형진
# 전화번호를 입력하세요. => 01000000000
# 주소를 입력하세요. => 건영아파트
# 메모할 것을 입력하세요. => 이것은 테스트입니다.
# (1, '한형진', '01000000000', '건영아파트', 'Mon Sep 19 16:40:10 2022', '이것은 테스트입니다.')
# (2, '한형주', '01011111111', '건영아파트', 'Mon Sep 19 16:47:54 2022', '이거슨 동생')