import os, time
# 경로 확인 모듈
if __name__ == '__main__':
    print(os.path.join(os.getcwd(), 'test'))
    # C:\Users\han12\OneDrive\Desktop\AIschool\Python\AI_Source\AI_01\1_Python\modules\test

    os.chdir('c:\\Windows')
    print(os.listdir(os.getcwd()))
    # ['addins', 'appcompat', 'apppatch', 'AppReadiness'...]

    print('\n----------- 1. -----------')
    secs = time.time()
    print(secs)

    print('\n----------- 2. -----------')
    tm = time.localtime(secs)
    print('년 (tm.tm_year) :', tm.tm_year)
    print('월 (tm.tm_mon) :', tm.tm_mon)
    print('일 (tm.tm_mday) :', tm.tm_mday)
    print('시 (tm.tm_hour) :', tm.tm_hour)
    print('분 (tm.tm_min) :', tm.tm_min)
    print('초 (tm.tm_sec) :', tm.tm_sec)
    print(tm)

    print('\n----------- 3. -----------')
    tm = time.localtime(secs)
    string = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)
    print(string)

    print('\n----------- 4. -----------')
    string = '2019-11-30 02:35:26 PM'
    tm = time.strptime(string, '%Y-%m-%d %I:%M:%S %p')
    print(tm)

    print('\n----------- 5. -----------')
    string = time.ctime(secs)
    print(string)

    print('\n----------- 6. -----------')
    print('Before')
    time.sleep(3)
    print('After 3 Seconds')
    # ----------- 1. -----------
    # 1663558765.9019258
    #
    # ----------- 2. -----------
    # 년 (tm.tm_year) : 2022
    # 월 (tm.tm_mon) : 9
    # 일 (tm.tm_mday) : 19
    # 시 (tm.tm_hour) : 12
    # 분 (tm.tm_min) : 39
    # 초 (tm.tm_sec) : 25
    # time.struct_time(tm_year=2022, tm_mon=9, tm_mday=19, tm_hour=12, tm_min=39, tm_sec=25, tm_wday=0, tm_yday=262, tm_isdst=0)
    #
    # ----------- 3. -----------
    # 2022-09-19 12:39:25 PM
    #
    # ----------- 4. -----------
    # time.struct_time(tm_year=2019, tm_mon=11, tm_mday=30, tm_hour=14, tm_min=35, tm_sec=26, tm_wday=5, tm_yday=334, tm_isdst=-1)
    #
    # ----------- 5. -----------
    # Mon Sep 19 12:39:25 2022
    #
    # ----------- 6. -----------
    # Before
    # 3초 후...
    # After 3 Seconds
    #
    # Process finished with exit code 0

from datetime import timedelta, timezone, date, time, datetime

if __name__ == '__main__':
    print(timedelta(days=7, hours=17, minutes=30))
    # 7 days, 17:30:00

    print(timezone(timedelta(hours=9)))
    # UTC+09:00

    today = date.today()
    print('today.isoformat() :', today.isoformat())
    print('today.fromisoformat(2022-09-19)) :', today.fromisoformat('2022-09-19'))
    print('today.today.weekday() :', today.weekday())
    print('today.isoweekday() :', today.isoweekday())
    print('today.replace(year=2023) :', today.replace(year=2023))
    # today.isoformat() : 2022-09-19
    # today.fromisoformat(2022-09-19)) : 2022-09-19
    # today.today.weekday() : 0
    # today.isoweekday() : 1
    # today.replace(year=2023) : 2023-09-19

    print(time(13, 42, 35))
    print('time.fromisoformat(13:42:35.458+09:00) :', time.fromisoformat('13:42:35.458+09:00'))
    t = time(13, 42, 35, 458000, tzinfo=timezone(timedelta(hours=9)))
    print('t.isoformat() :', t.isoformat())
    print('t.hour() :', t.hour)
    print('t.minute() :', t.minute)
    print('t.second() :', t.second)
    print('t.microsecond() :', t.microsecond)
    # t.isoformat() : 13:42:35.458000+09:00
    # t.hour() : 13
    # t.minute() : 42
    # t.second() : 35
    # t.microsecond() : 458000

    print(datetime(2022, 9, 19, 13, 26, 23))
    d = date(2022, 9, 19)
    t = time(13, 26, 23)
    print(datetime.combine(d, t))
    print(datetime.now())
    print(datetime.now().strftime('%Y/%m/%d'))
    print(datetime.strptime('2022/09/19', '%Y/%m/%d'))
    # 2022-09-19 13:26:23
    # 2022-09-19 13:26:23
    # 2022-09-19 14:31:33.608349
    # 2022/09/19
    # 2022-09-19 00:00:00

import random

if __name__ == '__main__':
    print('\n----------- 1. -----------')
    print(random.random()) # 0 ~ 1 사이의 난수 생성
    print('\n----------- 2. -----------')
    print(random.uniform(1, 10)) # 1 ~ 10 사이의 난수 생성
    print('\n----------- 3. -----------')
    print(random.randint(1, 10)) # 1부터 10 사이의 정수형 난수 반환
    print('\n----------- 4. -----------')
    print(random.randrange(0, 100, 2)) # 0부터 100 사이의 짝수 중(2 증가) 하나 선택
    print('\n----------- 5. -----------')
    print(random.choice('abcdefghijklmn')) # abcdefghijklmn 중 하나 선택
    print('\n----------- 6. -----------')
    print(random.sample([1, 2, 3, 4, 5], 3)) # 해당 배열에서 랜덤한 수 3개 선택
    print('\n----------- 7. -----------') # 해당 배열 셔플
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(items)
    print(items)
    # ----------- 1. -----------
    # 0.3410176613425868
    #
    # ----------- 2. -----------
    # 3.6819928095864336
    #
    # ----------- 3. -----------
    # 8
    #
    # ----------- 4. -----------
    # 64
    #
    # ----------- 5. -----------
    # k
    #
    # ----------- 6. -----------
    # [5, 1, 4]
    #
    # ----------- 7. -----------
    # [5, 7, 9, 8, 2, 4, 1, 3, 10, 6]