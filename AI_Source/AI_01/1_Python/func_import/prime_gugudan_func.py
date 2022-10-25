def input_num():
    num_1 = int(input('첫 번째 숫자를 입력하세요. : '))
    num_2 = int(input('두 번째 숫자를 입력하세요. : '))
    return num_1, num_2
# return 값이 여러 개인 경우, 튜플 형태로 패킹이 발생

def min_max_num(num_1, num_2):
    if (num_1 > num_2):
        min_num = num_2
        max_num = num_1
    elif (num_2 > num_1):
        min_num = num_1
        max_num = num_2
    return min_num, max_num
# return 값이 여러 개인 경우, 튜플 형태로 패킹이 발생

def print_cal(min, max):
    for dan in range(min, max + 1):
        print('----%d단----' % dan, end='     ')

    print('\n')

    for mul in range(1, 10):
        for dan in range(min, max + 1):
            print('%d * %d = %2d' % (dan, mul, dan * mul), end='     ')
        print('\n')
# print로 출력을 직접 하는 함수이기 때문에 return 생략 가능

def print_prime_num(min, max):
    count = 0
    for prime_num in range(min, max + 1):
    # 소수의 범위 지정
        for i in range(2, prime_num):
        # 소수는 1을 제외한 2부터 범위가 지정된 prime_num까지 반복문 실행
            if prime_num % i == 0:
            # prime_num과 i의 나머지가 0일 시에는 반복문 종료
                break
        else:
        # prime_num과 i의 나머지가 0이 아닐 시 출력
            print('%5d' % prime_num, end='')
            count += 1
            # 소수의 개수 카운트
            if count % 10 == 0:
            # 소수의 개수가 10의 배수이면 줄 바꿈 실행
                print('\n')

    print('\n')

    print('소수의 총 개수는 %d개 입니다.' % (count))
