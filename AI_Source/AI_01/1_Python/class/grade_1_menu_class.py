from grade_class import Grade

def menu_func():
    print(' ----메뉴----')
    print('1. 성적정보 입력')
    print('2. 성적정보 확인')
    print('3. 성적정보 조회')
    print('4. 성적정보 수정')
    print('5. 성적정보 삭제')
    print('6. 프로그램 종료')
def input_func(lis):
    obj = Grade()
    obj.setInfo()
    obj.setSum()
    obj.setAvg()
    obj.setGrade()
    lis.append(obj)
    print('-----------------------------------------------------------------------------')
def output_func(lis):
    obj = Grade()
    total_avg = 0
    obj.print_board()
    for data in lis:
        total_avg += data.avg
        data.result_print()
    print('-----------------------------------------------------------------------------')
    print('학생 수 : %d / 학생 평균 : % .2f' % (len(lis), total_avg / int(len(lis))))
    print('성적 데이터 출력이 종료됩니다.\n')

def show_func(lis):
    id_select = input('성적을 조회할 학번을 입력하세요. : ')
    for data in lis:
        if id_select == data.id:
            data.print_board()
            data.result_print()
            print('-----------------------------------------------------------------------------')
            print('\n해당 학번의 정보를 조회합니다.')
            break
    else:
        print('\n성적을 조회할 학번이 없습니다.')
def update_func(lis):
    id_select = input('성적을 수정할 학번을 입력하세요. : ')
    for data in lis:
        if id_select == data.id:
            data.kor = int(input('국어 점수를 입력하세요. => '))
            data.eng = int(input('영어 점수를 입력하세요. => '))
            data.math = int(input('수학 점수를 입력하세요. => '))
            data.sum = data.kor + data.eng + data.math
            data.avg = data.sum / 3
            data.setGrade()
            print('\n해당 학번의 정보가 수정되었습니다.')
            break
    else:
        print('\n성적을 수정할 학번이 없습니다.')
def delete_func(lis):
    id_select = input('성적을 삭제할 학번을 입력하세요. : ')
    for data in lis:
        if id_select == data.id:
            lis.remove(data)
            print('\n해당 학번의 정보가 삭제되었습니다.')
            break
    else:
        print('\n성적을 삭제할 학번이 없습니다.')

if __name__ == '__main__':
    lis = []
    while True:
        menu_func()
        try:
            menu_select = int(input('메뉴를 선택하세요. : '))
        except:
            print('메뉴 선택은 숫자만 가능합니다.\n')
            continue
        if menu_select == 1:
            input_func(lis)
        elif menu_select == 2:
            output_func(lis)
        elif menu_select == 3:
            show_func(lis)
        elif menu_select == 4:
            update_func(lis)
        elif menu_select == 5:
            delete_func(lis)
        elif menu_select == 6:
            print('\n프로그램을 종료합니다.')
            break
        else:
            print('\n메뉴를 다시 선택해 주세요.\n')