# 읽기는 불가능하며 출력하기만 가능
import xlsxwriter

workBook = xlsxwriter.Workbook('xlsxwriter2.xlsx')
ws = workBook.add_worksheet('Grade') # 워크시트 추가

data = [('홍길동', 80, 90, 70), ('이기자', 90, 60, 80), ('강기자', 80, 80, 70)]

row = 0 # xlsxwriter는 첫 번째 행이 0부터 시작
col = 0 # xlsxwriter는 첫 번째 열이 0부터 시작

"""
for name, kor, eng, math in data:
    ws.write(row, col, name)
    # r(0)행 c(0)열 위치의 데이터를 name으로 언패킹
    ws.write(row, col + 1, kor)
    ws.write(row, col + 2, eng)
    ws.write(row, col + 3, math)
    row += 1
"""

for val in data:
    for i in range(0, 4):
        ws.write(row, col+i, val[i])
    row += 1

ws.write(row, 0, '합계')
ws.write(row, 1, '=sum(B1:B3)')
ws.write(row, 2, '=sum(C1:C3)')
ws.write(row, 3, '=sum(D1:D3)')

workBook.close()