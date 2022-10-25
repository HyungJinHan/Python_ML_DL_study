import csv

f = open('data_01.csv', 'wt', encoding='utf-8', newline='')
# quotechar = '' # 데이터를 묶을 문자 지정
# csv.QUOTE_ALL # 모두 사용하겠다는 의미
# wr = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
wr = csv.writer(f, delimiter=',', quotechar='"')
wr.writerow([73, 80, 75, 152])
wr.writerow([93, 88, 93, 185])
wr.writerow([89, 91, 90, 180])
wr.writerow([96, 98, 100, 196])
wr.writerow([73, 66, 70, 142])
wr.writerow([53, 46, 55, 101])
wr.writerow([69, 74, 77, 149])
wr.writerow([47, 56, 60, 115])
wr.writerow([87, 79, 90, 175])
f.close()