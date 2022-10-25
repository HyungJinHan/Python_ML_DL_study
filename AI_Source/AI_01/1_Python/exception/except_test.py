try:
    a = [1, 2, 3]
    print(a[4])
    print(a[0] / 0)
except ZeroDivisionError:
    print('ZeroDivisionError : 0으로 나누었습니다.')
except IndexError:
    print('IndexError : 인덱스 번호가 잘못되었습니다.')
except:
    print('except : 기타 에러가 발생했습니다.')

# ------------------------------------------------------------------------------------------

def divide(m, n):
    try:
        result = m / n
    except ZeroDivisionError:
        print('ZeroDivisionError : 0으로 나눌 수 없습니다.')
    except:
        print('ZeroDivisionError 이외의 에러가 발생했습니다.')
    else:
        return result
    finally:
        print('------------ 결과를 출력합니다. ------------')

# ------------------------------------------------------------------------------------------

def userid(lang):
    if lang == '파이썬':
        raise Exception('Python')
    elif lang == '자바':
        raise Exception('Java')
    elif lang == '자바스크립트':
        raise Exception('JavaScript')
    else:
        print(lang)

if __name__ == '__main__':
    # res = divide(
    #     input('첫 번째 숫자를 입력해주세요. => '),
    #     input('두 번째 숫자를 입력해주세요. => ')
    # )
    res = divide(5, 5)
    print(res)
    print()

    try:
        userid(input('배우는 언어를 작성해주세요. : '))
    except Exception as e:
        print(e.args[0])