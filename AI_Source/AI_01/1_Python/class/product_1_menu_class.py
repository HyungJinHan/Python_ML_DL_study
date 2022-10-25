from product_class import Product

def menu_func():
    print(' ----메뉴----')
    print('1. 상품정보 입력')
    print('2. 상품정보 확인')
    print('3. 상품정보 조회')
    print('4. 상품정보 수정')
    print('5. 상품정보 삭제')
    print('6. 프로그램 종료')
def input_func(lis):
    obj = Product()
    obj.info()
    obj.priceSum()
    lis.append(obj)
    print('-----------------------------------------------------------------------------')
def output_func(lis):
    obj = Product()
    total_price = 0
    obj.print_board()
    for data in lis:
        total_price += data.productTotalPrice
        data.resultPrint()
    print('-----------------------------------------------------------------------------')
    print('등록된 제품 수 : %d / 등록된 제품 총 금액 : %s' % (len(lis), format(total_price, ',')))
    print('제품 데이터 출력이 종료됩니다.\n')
def show_func(lis):
    id_select = input('조회할 제품 코드를 입력하세요. : ')
    for data in lis:
        if id_select == data.productId:
            data.print_board()
            data.resultPrint()
            print('-----------------------------------------------------------------------------')
            break
    else:
        print('\n조회할 제품 코드가 없습니다.')
def update_func(lis):
    id_select = input('수정할 제품 코드를 입력하세요. : ')
    for data in lis:
        if id_select == data.productId:
            data.productName = input('제품 명을 입력하세요. => ')
            data.productCount = int(input('제품 수량을 입력하세요. => '))
            data.productPrice = int(input('제품 단가를 입력하세요. => '))
            data.productTotalPrice = data.productCount * data.productPrice
            print('-----------------------------------------------------------------------------')
            break
    else:
        print('\n수정할 제품 코드가 없습니다.')
def delete_func(lis):
    id_select = input('삭제할 제품 코드를 입력하세요. : ')
    for data in lis:
        if id_select == data.productId:
            lis.remove(data)
            break
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