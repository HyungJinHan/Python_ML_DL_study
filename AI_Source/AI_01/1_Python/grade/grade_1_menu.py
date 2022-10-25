def menu_func():
    print(' ----메뉴----')
    print('1. 성적정보 입력')
    print('2. 성적정보 확인')
    print('3. 성적정보 조회')
    print('4. 성적정보 수정')
    print('5. 성적정보 삭제')
    print('6. 프로그램 종료')

def input_func(lis):
    dic_i = {}

    dic_i['학번'] = input('학번을 입력하세요. => ')
    dic_i['이름'] = input('이름을 입력하세요. => ')

    dic_i['국어 점수'] = int(input('국어 점수를 입력하세요. => '))
    dic_i['영어 점수'] = int(input('영어 점수를 입력하세요. => '))
    dic_i['수학 점수'] = int(input('수학 점수를 입력하세요. => '))

    dic_i['합계'] = dic_i['국어 점수'] + dic_i['영어 점수'] + dic_i['수학 점수']

    dic_i['평균'] = dic_i['합계'] / 3

    if dic_i['평균'] >= 90:
        dic_i['등급'] = '수'
    elif 80 <= dic_i['평균'] < 90:
        dic_i['등급'] = '우'
    elif 70 <= dic_i['평균'] < 80:
        dic_i['등급'] = '미'
    elif 60 <= dic_i['평균'] < 70:
        dic_i['등급'] = '양'
    else:
        dic_i['등급'] = '가'

    lis.append(dic_i)
    print('-----------------------------------------------------------------------------')

def output_func(lis):
    total_avg = 0

    print('\n\t\t\t\t\t\t\t --- 성적표 ---')

    print('-----------------------------------------------------------------------------')

    print('  학번        이름       국어     영어    수학     총점     평균       등급')

    print('-----------------------------------------------------------------------------')

    for data in lis:
        total_avg += data["평균"]

        # list의 dic_i의 key값에 접근해서 요소의 수 만큼 for문으로 반복 출력
        print('%4s     %3s     %3d     %3d     %3d     %3d     %5.2f     %2s' %
              (
                  data['학번'],
                  data['이름'],
                  data['국어 점수'],
                  data['영어 점수'],
                  data['수학 점수'],
                  data['합계'],
                  data['평균'],
                  data['등급']
              )
              )
    print('-----------------------------------------------------------------------------')

    print('학생 수 : %d / 학생 평균 : % .2f' % (len(lis), total_avg / int(len(lis))))
    print('성적 데이터 출력이 종료됩니다.')

def show_func(lis):
    id_select = input('성적을 조회할 학번을 입력하세요. : ')
    for data in lis:
        if id_select == data['학번']:
            print('\n\t\t\t\t\t\t\t --- 성적표 ---')

            print('-----------------------------------------------------------------------------')

            print('  학번        이름       국어     영어    수학     총점     평균       등급')

            print('-----------------------------------------------------------------------------')

            print('%4s     %3s     %3d     %3d     %3d     %3d     %5.2f     %2s' %
                  (
                      data['학번'],
                      data['이름'],
                      data['국어 점수'],
                      data['영어 점수'],
                      data['수학 점수'],
                      data['합계'],
                      data['평균'],
                      data['등급']
                  )
                  )

            print('-----------------------------------------------------------------------------')
    else:
        print('\n성적을 조회할 학번이 없습니다.')

def update_func(lis):
    id_select = input('성적을 수정할 학번을 입력하세요. : ')

    for data in lis:
        if id_select == data['학번']:
            data['국어 점수'] = int(input('국어 점수를 입력하세요. => '))
            data['영어 점수'] = int(input('영어 점수를 입력하세요. => '))
            data['수학 점수'] = int(input('수학 점수를 입력하세요. => '))

            data['합계'] = data['국어 점수'] + data['영어 점수'] + data['수학 점수']

            data['평균'] = data['합계'] / 3

            if data['평균'] >= 90:
                data['등급'] = '수'
            elif 80 <= data['평균'] < 90:
                data['등급'] = '우'
            elif 70 <= data['평균'] < 80:
                data['등급'] = '미'
            elif 60 <= data['평균'] < 70:
                data['등급'] = '양'
            else:
                data['등급'] = '가'
    else:
        print('\n성적을 수정할 학번이 없습니다.')

def delete_func(lis):
    id_select = input('성적을 삭제할 학번을 입력하세요. : ')
    for data in lis:
        if id_select == data['학번']:
            lis.remove(data)
    else:
        print('\n성적을 삭제할 학번이 없습니다.')

if __name__ == '__main__':
    lis = []

    while True:
        menu_func()

        menu_select = int(input('메뉴를 선택하세요. : '))

        if menu_select == 1:
            input_func(lis)
        elif menu_select == 2:
            output_func(lis)
        elif menu_select == 3:
            show_func(lis)
            print('\n해당 학번의 정보를 조회합니다.')
        elif menu_select == 4:
            update_func(lis)
            print('\n해당 학번의 정보가 수정되었습니다.')
        elif menu_select == 5:
            delete_func(lis)
            print('\n해당 학번의 정보가 삭제되었습니다.')
        elif menu_select == 6:
            print('\n프로그램을 종료합니다.')
            break
        else:
            print('\n메뉴를 다시 선택해 주세요.')
