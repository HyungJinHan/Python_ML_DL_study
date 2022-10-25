dic = {}

id = input('학번을 입력하세요. => ')
name = input('이름을 입력하세요. => ')

kor_grade = int(input('국어 점수를 입력하세요. => '))
eng_grade = int(input('영어 점수를 입력하세요. => '))
math_grade = int(input('수학 점수를 입력하세요. => '))

dic['학번'] = id
dic['이름'] = name
dic['국어 점수'] = kor_grade
dic['영어 점수'] = eng_grade
dic['수학 점수'] = math_grade

total = dic['국어 점수'] + dic['영어 점수'] + dic['수학 점수']

dic['합계'] = total

avg = dic['합계'] / 3

dic['평균'] = avg

if avg >= 90:
    grade = '수'
elif 80 <= avg < 90:
    grade = '우'
elif 70 <= avg < 80:
    grade = '미'
elif 60 <= avg < 70:
    grade = '양'
else:
    grade = '가'

dic['등급'] = grade

print(dic)

print('\n\t\t\t\t\t\t\t --- 성적표 ---')

print('-----------------------------------------------------------------------------')

print('  학번        이름       국어     영어    수학     총점     평균       등급')

print('-----------------------------------------------------------------------------')

print('%4s     %3s     %3d     %3d     %3d     %3d     %5.2f     %2s' %
      (
        dic['학번'],
        dic['이름'],
        dic['국어 점수'],
        dic['영어 점수'],
        dic['수학 점수'],
        dic['합계'],
        dic['평균'],
        dic['등급']
      )
     )