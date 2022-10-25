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

if __name__ == '__main__':
    num_1, num_2 = input_num()
    # 패킹된 튜플을 언패킹하는 작업

    min_num, max_num = min_max_num(num_1, num_2)
    # 패킹된 튜플을 언패킹하는 작업

    print_cal(min_num, max_num)
