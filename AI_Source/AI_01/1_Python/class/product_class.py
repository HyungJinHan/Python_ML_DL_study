class Product:
    def __init__(self):
        self._productId = ''
        self._productName = ''
        self._productCount = 0
        self._productPrice = 0
        self._productTotalPrice = 0
        print('객체가 생성되었습니다.')
        # 여기서의 self는 생성된 객체의 주소를 말함
        # 쉽게 말해 그 시점의 자기 자신을 의미
    def info(self):
        self.productId = input('제품 코드를 입력하세요. => ')
        self.productName = input('제품 명을 입력하세요. => ')
        self.productCount = int(input('제품 수량을 입력하세요. => '))
        self.productPrice = int(input('제품 단가를 입력하세요. => '))
    def priceSum(self):
        self.productTotalPrice = self.productCount * self.productPrice
    def resultPrint(self):
        print('%10s %10s %10d %10d %10s'
              % (self.productId,
                 self.productName,
                 self.productCount,
                 self.productPrice,
                 format(self.productTotalPrice, ','))
              )
    def print_board(self):
        print('\n\t\t\t\t\t\t\t --- 제품 정보 ---')
        print('-----------------------------------------------------------------------------')
        print('%10s %10s %10s %10s %10s'
              % ('제품 코드', '제품 명', '제품 수량', '제품 단가', '판매 금액')
              )
        print('-----------------------------------------------------------------------------')