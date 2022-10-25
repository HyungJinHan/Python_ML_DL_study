import csv

f = open('output.csv', 'wt', encoding='utf-8', newline='')
# quotechar = '' # 데이터를 묶을 문자 지정
# csv.QUOTE_ALL # 모두 사용하겠다는 의미
# wr = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
wr = csv.writer(f, delimiter=',', quotechar='"')
wr.writerow((1, '정상수', False))
wr.writerow([2, '명사수', True])
f.close()