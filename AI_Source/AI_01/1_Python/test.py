a = "MBC"
b = "KBS"
c = 'Python'
d = 'GwangjuAIschool'

print(c[0])
print(c[-1])
print((a + b) * 3)
print(d[:7])
print(d[7:])
print(d[5:7])
print(d[-6:])

print('Hello\nPython!')
# Hello
# Python!

print('Hello' + 'Python!')
# HelloPython!

print('Hello', 'Python!')
# Hello Python!

print('Hello', 'Python!', sep='#')
# Hello#Python!

print('Hello', end=', ')
print('Python', end='!\n')
# Hello, Python!

print('I am Groot %d' % 5)
# I am Groot 5

print('I am %s %d' % ('Groot', 10))
# I am Groot 10

num = 7
print('I am %s %d' % ('Groot', num))
# I am Groot 7

print('I am %s %s' % ('Groot', num))
# I am Groot 7

print('I am %s %s%c' % ('Groot', num, '!'))
# I am Groot 7!

print('%d * %d = %d' % (10, 10, 100))
# 10 * 10 = 100

print('[%5d] * [%5d] = [%5d]' % (10, 10, 100))
# [   10] * [   10] = [  100]

print('[%-5d] * [%-5d] = [%-5d]' % (10, 10, 100))
# [10   ] * [10   ] = [100  ]

print('원주율은 %f입니다.' % 3.141592)
# 원주율은 3.141592입니다.

print('원주율은 %.2f입니다.' % 3.141592)
# 원주율은 3.14입니다.

print('소수 %1.2f입니다.' % 3123123.141592)
# 소수 3123123.14입니다.
# 앞의 정수의 경우 총 자리가 부족하더라도 자동으로 전부 배치

print('제 이름은 {}입니다.'.format('한형진'))
# 제 이름은 한형진입니다.

print('{1}! {0}점 입니다.'.format(500, '그리핀도르'))
# 그리핀도르! 500점 입니다.

print('[{:>10}]'.format('&'))
# [         &]

print('[{:<10}]'.format('&'))
# [&         ]

print('[{:<.3f}]'.format(123.456789))
# [123.457]
# 소수점 3자리 이후로 반올림 처리

print('[{:20,}]'.format(1234567890))
# [       1,234,567,890]

print('[{:,}]'.format(1234567890))
# [1,234,567,890]

print('hello'.upper())
# HELLO

print('HELLO'.lower())
# hello

print('       [hello]    '.upper().lstrip())
# [HELLO]'    ' -> 공백임

print('       [HELLO]    '.lower().rstrip())
#        [hello]

print('       [hello]    '.upper().strip())
# [HELLO]

print('C is Today\'s Studying Language'.replace('C', 'Python'))
# Python is Today's Studying Language

print('C is Today\'s Studying Language'.replace('c', 'Python'))
# C is Today's Studying Language
# 대소문자 중요

print('ABC DEF YOU'.lower().split())
# ['abc', 'def', 'you']

print('abc,def,you'.upper().split(','))
# ['ABC', 'DEF', 'YOU']

testList = [1, 2, 3, 4, 5, 'Python']

print(testList[0:3])
# [1, 2, 3]

print(testList[5])
# Python

print(testList[5][0:2])
# Py

tL1 = testList[:3]

print(tL1)
# [1, 2, 3]

tL2 = testList[-2:]

print(tL2)
# [5, 'Python']

# testList[0] = 'JavaScript'

# print(testList)
# ['JavaScript', 2, 3, 4, 5, 'Python']
# 1은 쓰레기 객체로 관계가 끊기며 그 자리에 'JavaScript'가 들어감

sortList = ['a', 'Dfw', 'bcc', 'cwe', 'ESda', 'hyf']

sortList.sort()
print(sortList)
# ['Dfw', 'ESda', 'a', 'bcc', 'cwe', 'hyf']
# 기본적으로 대문자부터 오름차순으로 정렬 (코드상의 정렬)

sortList.sort(key=str.upper)
print(sortList)
# ['a', 'bcc', 'cwe', 'Dfw', 'ESda', 'hyf']
# 단순한 알파벳 순으로 정렬

sortList.sort(key=str.upper, reverse=True)
print(sortList)
# ['hyf', 'ESda', 'Dfw', 'cwe', 'bcc', 'a']
# 단순한 알파벳의 내림차 순으로 정렬

dat = [('han', 'C', 10), ('hyung', 'A', 13), ('jin', 'B', 7)]

dat.sort(key=lambda score: score[1])
print(dat)
# [('hyung', 'A', 13), ('jin', 'B', 7), ('han', 'C', 10)]
# 두 번째인 알파벳을 기준으로 정렬

dat.sort(key=lambda student: student[0])
print(dat)
# [('han', 'C', 10), ('hyung', 'A', 13), ('jin', 'B', 7)]
# 첫 번째인 이름을 기준으로 정렬

dat.sort(key=lambda age: age[2])
print(dat)
# [('jin', 'B', 7), ('han', 'C', 10), ('hyung', 'A', 13)]
# 세 번째인 나이를 기준으로 정렬

aa = [1, 2, 3, 4, 5]

aa.append(6)
print(aa)
# [1, 2, 3, 4, 5, 6]

aa.sort(reverse=True)
print(aa)
# [6, 5, 4, 3, 2, 1]

aa.append([7, 8])
print(aa)
# [6, 5, 4, 3, 2, 1, [7, 8]]

print(aa.index([7, 8]))
# 6 (값의 위치를 인덱스로 출력)

aa.insert(1, 10)
print(aa)
# [6, 10, 5, 4, 3, 2, 1, [7, 8]]
# 인덱스 1번째 자리에 10을 삽입

aa.remove([7, 8])
print(aa)
# [6, 10, 5, 4, 3, 2, 1]

print(aa.pop(0))
# 6
print(aa)
# [10, 5, 4, 3, 2, 1]
# 인덱스 0번째인 6을 반환 후 제거

aa.insert(5, 10)
print(aa.count(10))
# 2 (10을 추가 후 10의 개수인 2 출력)

aa.extend([6, 7, 8, 9])
print(aa)
# [10, 5, 4, 3, 2, 10, 1, 6, 7, 8, 9]

t1 = ()
t2 = (1,)
t2_1 = (1)
t3 = (1, 2, 3)
t4 = 1, 2, 3

print(type(t2))
# <class 'tuple'>

print(type(t2_1))
# <class 'int'>

print(type(t4))
# <class 'tuple'>
# (1, 2, 3) 튜플의 형태로 출력

a, b, c = t4
print(a, b, c)
# 1 2 3
# 튜플은 데이터의 개수만큼 변수가 지정되면 자동으로 하나씩 지정됨
# unpacking이라고 함

t5 = (1, 10.5, 'Python')
print(t5[2])
# Python

print(t5[2][0:4])
# Pyth

dic = {'id': 'Han', 'pw': 1210}
print(dic)
# {'id': 'Han', 'pw': 1210}

print(dic['id'], dic['pw'])
# Han 1210

dic['email'] = 'han1210_36@naver.com'
print(dic['email'])
# han1210_36@naver.com

dic['address'] = '광주'
print(dic)
# {'id': 'Han', 'pw': 1210, 'email': 'han1210_36@naver.com', 'address': '광주'}

del dic['address']
print(dic)
# {'id': 'Han', 'pw': 1210, 'email': 'han1210_36@naver.com'}

# ------------------------------------------------------------------------------------------

print(dic.keys())
# dict_keys(['id', 'pw', 'email'])
# 해당 딕셔너리의 key 값 조회

print(dic.values())
# dict_values(['Han', 1210, 'han1210_36@naver.com'])
# 해당 딕셔너리의 value 값 조회

print(dic.items())
# dict_items([('id', 'Han'), ('pw', 1210), ('email', 'han1210_36@naver.com')])
# 해당 딕셔너리의 key, value 값 조회

print(dic.get('id'), dic.get('pw'), dic.get('email'), dic.get('address'))
# Han 1210 han1210_36@naver.com None

print('id' in dic, 'address' in dic)
# True False
# 값이 존재하는지 체크

print(dic.clear())
# None
# 해당 딕셔너리의 데이터 지우기

# ------------------------------------------------------------------------------------------

set1 = set([1, 2, 3])
print(set1)
# {1, 2, 3}

set1 = set([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6])
print(set1)
# {1, 2, 3, 4, 5, 6}
# 집합(set)은 중복값 허용 X

set2 = set('Hello')
print(set2)
# {'e', 'l', 'o', 'H'}
# 자동 정렬 X

set3 = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
set4 = set([6, 7, 8, 9, 10, 11, 12, 13])
print(set3 & set4)
# {8, 9, 6, 7}
# 두 개의 집합(set)의 중복된 값 반환
# 여기서 ()은 형변환을 위한 cast 연산자라고 함

print(set3.intersection(set4))
# {8, 9, 6, 7}

print(set1 | set2 | set3 | set4)
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 'l', 'o', 'H', 'e'}
# 집합(set) 합친 후 반환

print(set1.union(set2).union(set3).union(set4))
# {1, 2, 3, 4, 5, 6, 7, 8, 'H', 9, 10, 11, 12, 13, 'e', 'o', 'l'}

print(set3 - set4)
# {1, 2, 3, 4, 5}
# 집합(set)끼리의 중복값 빼기

print(set3.difference(set4))
# {1, 2, 3, 4, 5}

print(set3 ^ set4)
# {1, 2, 3, 4, 5, 10, 11, 12, 13}
# 중복된 값을 제외한 나머지 값 반환

print(set3.symmetric_difference(set4))
# {1, 2, 3, 4, 5, 10, 11, 12, 13}

# ------------------------------------------------------------------------------------------

print(1 == 1)
# True
# ===는 사용 X

print(1 > 2)
# False

if [1, 2]:
    print('True')
else:
    print('False')
# True

# ------------------------------------------------------------------------------------------

listIn = [1, 2, 3, 4, 'a', 'h', 'Hello']

print(1 in listIn)
# True

print('hello' in listIn)
# False (대소문자 구별 X로 인해 존재 X)

listNum = {'one': 1, 'two': 2, 'three': 3}

print('one' in listNum)
# True

print('four' in listNum)
# False

a = 1
b = 7

print(a and b)
print(a & b)
print(a | b)
print(~a)

# ------------------------------------------------------------------------------------------

grade = float(4.5)
# input은 문자열로 반환하기 때문에 float를 사용해서 실수형으로 변경

if grade >= 4.3:
    print('장학금 수여 대상자 입니다.')
    print('수여를 위해 관계자와 연락하시기 바랍니다.\n')
else:
    print('장학금 수여 대상자가 아닙니다.\n')

# 4.3 이상일 시
# 장학금 수여 대상자 입니다.
# 수여를 위해 관계자와 연락하시기 바랍니다.

# 4.3 미만일 시
# 장학금 수여 대상자가 아닙니다.

data = int(10)
# input은 문자열로 반환하기 때문에 int를 사용해서 정수형으로 변경

if data % 2 == 0:
    print('입력된 값은 짝수입니다.')
else:
    print('입력된 값은 홀수입니다.')

print('짝수, 홀수 판독기 끝\n')

# 2 입력 시
# 입력된 값은 짝수입니다.
# 짝수, 홀수 판독기 끝

# 3 입력 시
# 입력된 값은 홀수입니다.
# 짝수, 홀수 판독기 끝

score = int(100)

if score > 100:
    print('점수는 100 이하로 입력할 수 있습니다.\n')
else:
    if score >= 90:
        print('수\n')
    else:
        if 80 <= score < 90:
            print('우\n')
        else:
            if 70 <= score < 80:
                print('미\n')
            else:
                if 60 <= score < 70:
                    print('양\n')
                else:
                    print('가\n')

if score > 100:
    print('점수는 100 이하로 입력할 수 있습니다.\n')
elif score >= 90:
    print('수\n')
elif 80 <= score < 90:
    print('우\n')
elif 70 <= score < 80:
    print('미\n')
elif 60 <= score < 70:
    print('양\n')
else:
    print('가\n')

count_a = 1
total_a = 0

while count_a <= 100:
    total_a = total_a + count_a
    count_a = count_a + 1
    if count_a == 10:
        break
else:
    print('덧셈 작업이 완료되었습니다.')

print('1부터 100까지의 합 :', total_a, '\n')

# 덧셈 작업이 완료되었습니다.
# 1부터 100까지의 합 : 5050

# break 결과
# 45

message = 'Hello!'
messages = ['Hello, World', '광주인공지능사관학교']
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
polygon = {'triangle': 2, 'rectangle': 1, 'line': 0}
color = {'red', 'green', 'blue'}

print('------------1------------')
for item in message:
    print(item)

print('------------2------------')
for item in messages:
    print(item)

print('------------3------------')
for item in numbers:
    print(item)

print('------------4------------')
for item in polygon:
    print(item, '=>', polygon[item])

print('------------5------------')
for item in color:
    print(item)
    for char in item:
        print(char)

# ------------1------------
# H
# e
# l
# l
# o
# !
# ------------2------------
# Hello, World
# 광주인공지능사관학교
# ------------3------------
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# ------------4------------
# 딕셔너리는 비순차지만, 최근 버전에서는 key를 입력한 순서대로 출력되도록 변경됨
# polygon[item] 사용
# triangle => 2
# rectangle => 1
# line => 0
# ------------5------------
# set은 비순차 개념이기 때문에 순서가 항상 랜덤
# blue
# b
# l
# u
# e
# green
# g
# r
# e
# e
# n
# red
# r
# e
# d

for val in range(1, 10):
    print('부와아아앙', val)

# 부와아아앙 1
# 부와아아앙 2
# 부와아아앙 3
# 부와아아앙 4
# 부와아아앙 5
# 부와아아앙 6
# 부와아아앙 7
# 부와아아앙 8
# 부와아아앙 9
# range()는 마지막 숫자 미만까지 반복 처리

for ran in range(0, 11, 2):
    print(ran)

# 0
# 2
# 4
# 6
# 8
# 10

for ran in range(11):
    print(ran)
else:
    print('0부터 10까지 출력했습니다.')

# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 0부터 10까지 출력했습니다.

lis_f = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [num * 3 for num in lis_f if num % 2 == 0]
print('1부터 10까지의 수에서 짝수만 3을 곱한 후 출력한 결과 :',result)
# 1부터 10까지의 수에서 짝수만 3을 곱한 후 출력한 결과 : [6, 12, 18, 24, 30]

for val in range(11):
    if val > 6:
        break
        if val > 3:
            break
    print(val)

# 0
# 1
# 2
# 3
# 4
# 5
# 6

for val in range(11):
    if val == 5:
        continue
    elif val == 8:
        continue
    print(val);

print('-------------------')

# 0
# 1
# 2
# 3
# 4
# 6
# 7
# 9
# 10

a_p = 100

if a_p > 10:
    pass
else:
    print(a_p)

# a_p가 100이기 때문에 아무것도 실행되지 않음

# ------------------------------------------------------------------------------------------

print(sorted([4, 2, 1, 3]))
print(sorted(['aaa', 'bbbb', 'ddddd', 'cc'], key=len))
print(sorted(['aaa', 'bbbb', 'ddddd', 'cc'], key=len, reverse=True))

# [1, 2, 3, 4]
# ['cc', 'aaa', 'bbbb', 'ddddd']
# ['ddddd', 'bbbb', 'aaa', 'cc']

print(len(['aaa', 'bbbb', 'ddddd', 'cc']))
print(len('Python'))

# 4
# 6

print(max([1, 2, 3, 10 ,50, 7, 9]))

# 50

def exp_2(a):
    return a*a
print(list(map(exp_2, [1, 2, 3, 4, 5])))

# [1, 4, 9, 16, 25]

for i, val in enumerate([' mbc', ' kbs', ' tvn']):
    print(i, val)

# 시작 값 생략
# 0  mbc
# 1  kbs
# 2  tvn

# 시작 값 5
# 5  mbc
# 6  kbs
# 7  tvn

# ------------------------------------------------------------------------------------------

def add_0(a, b):
    return a + b

print(add_0(b = 80, a = 8))
# 88

# print(add_0(b = 80, 8))
# Error - 키워드 인자는 기본 인자보다 뒤에 위치해야 함

def add_1(a, *b):
    sum = a
    for val in b:
        sum += val
    return sum

print(add_1(1, 10, 100, 1000))
# b를 튜플 형식으로 1, 10, 100, 1000라는 매개변수를 담고 더한 결과
# 1111

print(add_1(5, 50, 500, 5000, 50000))
# 55555

def add_2(a, **b):
    sum = a
    for val in b:
        sum += b[val]
    return sum, b

print(add_2(1000, Name=1, Gender=10, Age=100))
# (1006, {'Name': 1, 'Gender': 2, 'Age': 3})
# b는 딕셔너리 형태로 만들어지며, a는 b의 값과 1000의 합의 결과

def add_1_2(a, *b, **c):
    # 일반 인자 -> 가변 인자 -> 정의되지 않은 인자 순서로 사용
    sum = a
    for val in b:
        sum += val
    for val in c:
        sum += c[val]
    return sum, a, b, c

print(add_1_2(1000, 10000, 100000, 1000000, Name=1, Gender=10, Age=100))
# (1111111, 1000, (10000, 100000, 1000000), {'Name': 1, 'Gender': 10, 'Age': 100})
# a : a, b, c의 값의 합 결과 / b : 튜플 형태인 (10000, 100000, 1000000) / c : 딕셔너리 형태인 {'Name': 1, 'Gender': 10, 'Age': 100}

add_3 = lambda a, b, c: a + b + c

print(add_3(1, 10, 100))
# 111

def func_add_3(add):
    add(7, 70, 700)

func_add_3(lambda a, b, c: print(a + b + c))
# 777

def circle_area_1(r):
    # r은 형식 매개변수로 지역 변수로 작동됨
    # 함수가 끝나는 대로 소멸되는 변수
    result = 3.14 * (r ** 2)
    return result

if __name__ == '__main__':
    radius = 3
    area = circle_area_1(radius)
    print('반지름 : %d, 면적 : %.2f' % (radius, area))
    # 반지름 : 3, 면적 : 28.26

    # print(r)
    # Error
    # r은 Local 변수로 지정됐기 때문에 Global로써 사용 불가

pi = 3.1415

def circle_area_local_pi(r):
    pi = 3.14
    result = pi * (r ** 2)
    return result

def circle_area_global_pi(r):
    result = pi * (r ** 2)
    return result

def sum_areas(r):
    results = [circle_area_local_pi(r), circle_area_global_pi(r)]
    return sum(results)

if __name__ == '__main__':
    print('PI : ', pi)
    # Global 변수
    # PI :  3.1415

    print('Local pi 반지름 : ', 3, '면적 : ', circle_area_local_pi(3))
    # Local 변수 pi를 사용한 계산
    # Global pi 반지름 :  3 면적 :  28.26

    print('Global pi 반지름 : ', 3, '면적 : ', circle_area_global_pi(3))
    # Global 변수 pi를 사용한 계산
    # Local pi 반지름 :  3 면적 :  28.273500000000002

    print(sum_areas(3))
    # 56.533500000000004

def circle_area_2(r):
    global pi
    # 전역 변수를 참조해서 사용
    # 해당 함수가 실행되면 전역 변수의 값 자체도 변경됨

    pi = pi + 0.000092
    result = pi * (r ** 2)
    return result, pi

if __name__ == '__main__':
    print('PI :', pi)
    # PI :  3.1415
    # 원래의 전역 변수 값 출력

    result, pi = circle_area_2(3)
    # 언패킹 작업

    print('pi * (r ** 2)의 결과 =', result, '\n', '전역 변수인 pi를 참조해서 계산한 pi + 0.000092 값', pi)
    # pi * (r ** 2)의 결과 = 28.274328
    # 전역 변수인 pi를 참조해서 계산한 pi + 0.000092 값 3.141592

    print('PI :', pi)
    # PI :  3.141592
    # 전역 변수를 참조하여 계산하는 함수가 실행되면서 전역 변수의 값 자체도 변경

radius = 0

def circle_area_3(r, result):
    global radius
    area = 3.14 * (r ** 2)
    radius = r
    result(area)

if __name__ == '__main__':
    circle_area_3(3, lambda x: print('결과값 :', round(x, 1)))
    # 결과값 : 28.3
    print(radius)
    # 3

    circle_area_3(6, lambda x: print('결과값 :', round(x, 2)))
    # 결과값 : 113.04
    print(radius)
    # 6