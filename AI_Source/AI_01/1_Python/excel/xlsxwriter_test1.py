# 읽기는 불가능하며 출력하기만 가능
import xlsxwriter

workBook = xlsxwriter.Workbook('xlsxwriter1.xlsx')
ws = workBook.add_worksheet('Test_xlsxwriter') # 워크시트 추가

ws.write('A1', '젓 번째 값')
ws.write('A2', '두 번째 값')
ws.write('A3', '합계')
ws.write(3, 3, 'Test1')
ws.write(4, 4, 'Test2')
ws.write('B1', 10)
ws.write('B2', 20)
ws.write('B3', '=sum(B1:B2)')

workBook.close()