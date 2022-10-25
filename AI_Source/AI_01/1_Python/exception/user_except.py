class GradeException(Exception):
    def __init__(self, msg):
        self._message = msg

def inputGrade_func():
    grade = int(input('점수를 입력해주세요. => '))
    if grade < 0:
        raise GradeException('점수는 0점 이상부터 입력이 가능합니다.')
    elif grade > 100:
        raise GradeException('점수는 100점 이하까지 입력이 가능합니다.')
    else:
        return grade

if __name__ == '__main__':
    try:
        grade = inputGrade_func()
    except GradeException as e:
        print(e.args[0])
    else:
        print('입력한 점수는 %d입니다.' % grade)