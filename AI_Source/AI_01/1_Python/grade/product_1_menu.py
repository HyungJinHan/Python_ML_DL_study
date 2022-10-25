def menu_func():
    print(' ----메뉴----')
    print('1. 상품정보 입력')
    print('2. 상품정보 확인')
    print('3. 상품정보 조회')
    print('4. 상품정보 수정')
    print('5. 상품정보 삭제')
    print('6. 프로그램 종료')

def input_func(lis):
    dic_i = {}

    dic_i['제품 코드'] = input('제품 코드를 입력하세요. => ')
    dic_i['제품 명'] = input('제품 명을 입력하세요. => ')

    dic_i['제품 수량'] = int(input('제품 수량을 입력하세요. => '))
    dic_i['제품 단가'] = int(input('제품 단가을 입력하세요. => '))

    dic_i['판매 금액'] = dic_i['제품 수량'] * dic_i['제품 단가']

    lis.append(dic_i)
    print('-----------------------------------------------------------------------------')

def output_func(lis):
    total_price = 0

    print('\n\t\t\t\t\t\t\t --- 제품 보드 ---')

    print('-----------------------------------------------------------------------------')

    print('     제품 코드        제품 명         제품 수량      제품 단가       판매 금액')

    print('-----------------------------------------------------------------------------')

    for data in lis:
        total_price += data["판매 금액"]

        # list의 dic_i의 key값에 접근해서 요소의 수 만큼 for문으로 반복 출력
        print('%10s     %10s     %10d     %10d     %10d' %
              (
                  data['제품 코드'],
                  data['제품 명'],
                  data['제품 수량'],
                  data['제품 단가'],
                  data['판매 금액']
              )
              )

    print('-----------------------------------------------------------------------------')

    print('등록된 제품 수 : %d / 등록된 제품 총 금액 : %d' % (len(lis), total_price))
    print('제품 데이터 출력이 종료됩니다.')

def show_func(lis):
    id_select = input('조회할 제품 코드를 입력하세요. : ')
    for data in lis:
        if id_select == data['제품 코드']:
            print('\n\t\t\t\t\t\t\t --- 제품 보드 ---')

            print('-----------------------------------------------------------------------------')

            print('     제품 코드        제품 명         제품 수량      제품 단가       판매 금액')

            print('-----------------------------------------------------------------------------')

            print('%10s     %10s     %10d     %10d     %10d' %
                  (
                      data['제품 코드'],
                      data['제품 명'],
                      data['제품 수량'],
                      data['제품 단가'],
                      data['판매 금액']
                  )
                  )

            print('-----------------------------------------------------------------------------')
    else:
        print('\n조회할 제품 코드가 없습니다.')

def update_func(lis):
    id_select = input('수정할 제품 코드를 입력하세요. : ')

    for data in lis:
        if id_select == data['제품 코드']:
            data['제품 명'] = input('제품 명을 입력하세요. => ')
            data['제품 수량'] = int(input('제품 수량을 입력하세요. => '))
            data['제품 단가'] = int(input('제품 단가를 입력하세요. => '))

            data['판매 금액'] = data['제품 수량'] * data['제품 단가']
    else:
        print('\n수정할 제품 코드가 없습니다.')

def delete_func(lis):
    id_select = input('삭제할 제품 코드를 입력하세요. : ')
    for data in lis:
        if id_select == data['제품 코드']:
            lis.remove(data)
    else:
        print('\n삭제할 제품 코드가 없습니다.')

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
            print('\n해당 제품 코드의 정보를 조회합니다.')
        elif menu_select == 4:
            update_func(lis)
            print('\n해당 제품 코드의 정보가 수정되었습니다.')
        elif menu_select == 5:
            delete_func(lis)
            print('\n해당 제품 코드의 정보가 삭제되었습니다.')
        elif menu_select == 6:
            print('\n프로그램을 종료합니다.')
            break
        else:
            print('\n메뉴를 다시 선택해 주세요.')
