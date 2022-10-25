# 읽기는 불가능하며 출력하기만 가능
import xlsxwriter

workBook1 = xlsxwriter.Workbook('xlsxwriter_chart.xlsx')
ws = workBook1.add_worksheet()
chart = workBook1.add_chart({'type': 'column'})

ws.write('A1', '성적표')
ws.write('A2', '이름')
ws.write('B2', '국어')
ws.write('C2', '영어')
ws.write('D2', '수학')

data = [
    ('한형진', 100, 90, 95),
    ('전우진', 90, 60, 80),
    ('김성환', 80, 80, 70),
    ('김건', 70, 90, 50),
    ('문경현', 90, 90, 60),
    ('황기성', 100, 60, 80)
]

ws.write_row('A3', data[0])
# 행 기준으로 데이터 저장 / ws.write_column()은 열 기준
ws.write_row('A4', data[1])
ws.write_row('A5', data[2])
ws.write_row('A6', data[3])
ws.write_row('A7', data[4])
ws.write_row('A8', data[5])

chart.set_title({'name': '성적표'})
chart.set_x_axis({'name': '이름'})
chart.set_y_axis({'name': '점수'})

chart.add_series({'categories': '=Sheet1!$A$3:$A$8', 'values': '=Sheet1!$B$3:$B$8'})
chart.add_series({'categories': '=Sheet1!$A$3:$A$8', 'values': '=Sheet1!$C$3:$C$8'})
chart.add_series({'categories': '=Sheet1!$A$3:$A$8', 'values': '=Sheet1!$D$3:$D$8'})

ws.insert_chart('F1', chart)

workBook1.close()