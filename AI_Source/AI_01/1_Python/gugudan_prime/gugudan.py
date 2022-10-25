num_1 = int(input('첫 번째 숫자를 입력하세요. : '))
num_2 = int(input('두 번째 숫자를 입력하세요. : '))

if (num_1 > num_2):
    min_num = num_2
    max_num = num_1
elif (num_2 > num_1):
    min_num = num_1
    max_num = num_2

for dan in range(min_num, max_num + 1):
    print('----%d단----' % dan, end='     ')

print('\n')

for mul in range(1, 10):
    for dan in range(min_num, max_num + 1):
        print('%d * %d = %2d' % (dan, mul, dan * mul), end='     ')
    print('\n')