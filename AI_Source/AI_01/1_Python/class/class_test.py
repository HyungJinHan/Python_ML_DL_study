lis = []

class Grade:
    def __init__(self):
        self._id = ''
        self._name = ''
        self._kor = ''
        self._eng = ''
        self._math = ''
        self._sum = ''
        self._avg = ''
        self._grade = ''
        print('객체가 생성되었습니다.')
        # 여기서의 self는 생성된 객체의 주소를 말함
        # 쉽게 말해 그 시점의 자기 자신을 의미
    def setId(self, id):
        self._id = id
        print('학번이 변경되었습니다.')
    def setName(self, name):
        self._name = name
        print('이름이 변경되었습니다.')
    def setKor(self, kor):
        self._kor = kor
        print('국어 점수가 변경되었습니다.')
    def setEng(self, eng):
        self._eng = eng
        print('영어 점수가 변경되었습니다.')
    def setMath(self, math):
        self._math = math
        print('수학 점수가 변경되었습니다.')
    def result_print(self):
        print(
            'ID : %s / 이름 : %s / 국어 점수 : %3d / 영어 점수 : %3d / 수학 점수 : %3d'
            % (self._id, self._name, self._kor, self._eng, self._math)
        )
    # def __del__(self):
    #     print('객체가 소멸되었습니다.')

# class Car_1:
#     def __init__(self):
#         self.price = int(input('차의 가격을 입력해 주세요. => '))
#         self._zeroback = int(input('차의 제로백을 입력해 주세요. => '))
#         self.__color = input('차의 색상을 입력해 주세요. => ')

class Car_2:
    def __init__(self):
        self._price = 0
        self._zeroback = 0
        self._color = None
    def get_price(self):
        return self._price
    def set_price(self, value):
        self._price = value
    def get_zeroback(self):
        return self._zeroback
    def set_zeroback(self, value):
        self._zeroback = value
    def get_color(self):
        return self._color
    def set_color(self, value):
        self._color = value

class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name1(self):
        print('제 이름은 %s입니다.' % self.name)
    def get_age1(self):
        print('제 나이는 %d살입니다.' % self.age)

class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_name2(self):
        print('제 이름은 %s입니다.' % self.name)
    def get_age2(self):
        print('제 나이는 %d살입니다.' % self.age)

class Student(Person1, Person2):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        # 부모 클래스를 의미하며, 꼭 super를 지정해줘야 상속이 가능
        # 부모 클래스를 불러오는 함수는 항상 맨 처음에 지정을 먼저 해줘야 함
        self.grade = grade
    def get_grade(self):
        print('제 점수는 %d점입니다.' % self.grade)

# -------------------------------- 함수, 클래스 부분 --------------------------------

if __name__ == '__main__':

    # ---------- 성적 정보 입력 ----------
    obj = Grade()
    obj.setId(input('ID를 입력해 주세요. => '))
    obj.setName(input('이름을 입력해 주세요. => '))
    obj.setKor(int(input('국어 점수를 입력해 주세요. => ')))
    obj.setEng(int(input('영어 점수를 입력해 주세요. => ')))
    obj.setMath(int(input('수학 점수를 입력해 주세요. => ')))
    obj.result_print()

    # ---------- 차 정보 입력 (접근 제한) ----------
    # car_info_1 = Car_1()
    # print(car_info_1.price)
    # print(car_info_1._zeroback)
    # 접근은 가능하지만 정확한 사용법은 아님
    # print(car_info_1.__color)
    # Error

    # ---------- 차 정보 입력 ----------
    car_info_2 = Car_2()
    car_info_2.set_price(int(input('차의 가격을 입력해 주세요. => ')))
    car_info_2.set_zeroback(int(input('차의 제로백을 입력해 주세요. => ')))
    car_info_2.set_color(input('차의 색상을 입력해 주세요. => '))
    print('차의 가격 :', car_info_2.get_price())
    print('차의 제로백 :', car_info_2.get_zeroback())
    print('차의 색상 :', car_info_2.get_color())

    # ---------- 학생 정보 (상속) ----------
    stu_info = Student('한형진', 27, 100)
    stu_info.get_name1()
    stu_info.get_age1()
    stu_info.get_name2()
    stu_info.get_age2()
    stu_info.get_grade()
    # 제 이름은 한형진입니다.
    # 제 나이는 27살입니다.
    # 제 이름은 한형진입니다.
    # 제 나이는 27살입니다.
    # 제 점수는 100점입니다.