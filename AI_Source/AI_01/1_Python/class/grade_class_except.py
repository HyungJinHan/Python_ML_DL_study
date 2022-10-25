class Grade:
    def __init__(self):
        self._id = ''
        self._name = ''
        self._kor = 0
        self._eng = 0
        self._math = 0
        self._sum = 0
        self._avg = 0
        self._grade = ''
        print('객체가 생성되었습니다.')
        # 여기서의 self는 생성된 객체의 주소를 말함
        # 쉽게 말해 그 시점의 자기 자신을 의미
    def setInfo(self):
        self.id = input('학번을 입력하세요. => ')
        self.name = input('이름을 입력하세요. => ')
        while True:
            try:
                self.kor = int(input('국어 점수를 입력하세요. => '))
                if self.kor > 100:
                    print('\n국어 점수는 100점 이하로 입력해주세요.')
                    continue
                elif self.kor < 0:
                    print('\n국어 점수는 0점 이상으로 입력해주세요.')
                    continue
                else:
                    break
            except:
                print('\n국어 점수를 정수로 입력해주세요.')
                continue
            else:
                break
        while True:
            try:
                self.eng = int(input('영어 점수를 입력하세요. => '))
                if self.eng > 100:
                    print('\n영어 점수는 100점 이하로 입력해주세요.')
                    continue
                elif self.eng < 0:
                    print('\n영어 점수는 0점 이상으로 입력해주세요.')
                    continue
                else:
                    break
            except:
                print('\n영어 점수를 정수로 입력해주세요.')
                continue
            else:
                break
        while True:
            try:
                self.math = int(input('수학 점수를 입력하세요. => '))
                if self.math > 100:
                    print('\n수학 점수는 100점 이하로 입력해주세요.')
                    continue
                elif self.math < 0:
                    print('\n수학 점수는 0점 이상으로 입력해주세요.')
                    continue
                else:
                    break
            except:
                print('\n수학 점수를 정수로 입력해주세요.')
                continue
            else:
                break
    def setSum(self):
        self.sum = self.kor + self.eng + self.math
    def setAvg(self):
        self.avg = self.sum / 3
    def setGrade(self):
        if self.avg >= 90:
            self.grade = '수'
        elif 80 <= self.avg < 90:
            self.grade = '우'
        elif 70 <= self.avg < 80:
            self.grade = '미'
        elif 60 <= self.avg < 70:
            self.grade = '양'
        else:
            self.grade = '가'
    def result_print(self):
        print('%8s %8s %8d %8d %8d %8d %10.2f %7s'
              % (self.id, self.name, self.kor, self.eng, self.math, self.sum, self.avg, self.grade)
              )
    def print_board(self):
        print('\n\t\t\t\t\t\t\t --- 성적표 ---')
        print('-----------------------------------------------------------------------------')
        print('%8s %6s %7s %7s %7s %6s %7s %8s'
              % ('학번', '이름', '국어', '영어', '수학', '총점', '평균', '등급')
              )
        print('-----------------------------------------------------------------------------')

# -------------------------------- 함수, 클래스 부분 --------------------------------

if __name__ == '__main__':
    obj = Grade()
    obj.setInfo()
    obj.setSum()
    obj.setAvg()
    obj.setGrade()
    obj.print_board()
    obj.result_print()