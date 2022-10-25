import pymysql

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
        dbconn = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='bbs',
            charset='utf8'
        )
        dbcursor = dbconn.cursor()
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
        try:
            dbcursor.execute(
                'INSERT INTO grade_mysql (id, name, kor, eng, math, sum, avg, grade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                (self.id, self.name, self.kor, self.eng, self.math, self.sum, self.avg, self.grade))
        except:
            print('\n성적 입력에 오류가 있습니다.')
        else:
            dbconn.commit()
        finally:
            dbcursor.close()
            dbconn.close()

    def result_print(self):
        dbconn = pymysql.connect(
            host='localhost',
            user='root',
            password='123456',
            db='bbs',
            charset='utf8'
        )
        dbcursor = dbconn.cursor()
        dbcursor.execute('SELECT * FROM grade_mysql')
        res = dbcursor.fetchall()
        for row in res:
            print(str(row[0]) + '\t' + '\t' +
                  str(row[1]) + '\t' + '\t' +
                  str(row[2]) + '\t' + '\t' +
                  str(row[3]) + '\t' + '\t' +
                  str(row[4]) + '\t' + '\t' +
                  str(row[5]) + '\t' + '\t' +
                  str(row[6]) + '\t' + '\t' +
                  str(row[7]) + '\t' + '\t')
        dbconn.commit()
        dbcursor.close()
        dbconn.close()

    def print_board(self):
        print('\n\t\t\t\t\t\t\t --- 성적표 ---')
        print('-----------------------------------------------------------------------------')
        # print('%8s %6s %7s %7s %7s %6s %7s %8s'
        #       % ('학번', '이름', '국어', '영어', '수학', '총점', '평균', '등급')
        #       )
        print('ID \t 이름 \t 국어 점수 \t 영어 점수 \t 수학 점수 \t 총점 \t 평균 \t 등급')
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