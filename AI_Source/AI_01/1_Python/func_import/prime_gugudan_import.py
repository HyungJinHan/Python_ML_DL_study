# from prime_gugudan_func import input_num, min_max_num, print_cal, print_prime_num

import prime_gugudan_func

if __name__ == '__main__':
    num_1, num_2 = prime_gugudan_func.input_num()
    # 패킹된 튜플을 언패킹하는 작업

    min_num, max_num = prime_gugudan_func.min_max_num(num_1, num_2)
    # 패킹된 튜플을 언패킹하는 작업

    print('---------구구단---------')
    prime_gugudan_func.print_cal(min_num, max_num)

    print('---------소수 구하기---------')
    prime_gugudan_func.print_prime_num(min_num, max_num)
