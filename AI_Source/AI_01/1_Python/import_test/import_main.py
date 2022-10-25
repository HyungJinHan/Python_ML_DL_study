# import math

# print(math.sin(math.pi))
# 1.2246467991473532e-16
# pi의 사인(sin) 값 구하기

from math import sin, pi

if __name__ == '__main__':
    print(sin(pi))
    # 1.2246467991473532e-16

def message(val):
    print('Hello,', val)

if __name__ == '__main__':
    message('Python')

def add(a, b):
    return print(a + b)

if __name__ == '__main__':
    add(10, 20)
    # 30

def add1(a, b = 0):
    return print(a + b)

if __name__ == '__main__':
    add1(10) # 10
    add1(10, 20) # 30