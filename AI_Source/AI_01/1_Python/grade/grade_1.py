id = input('학번을 입력하세요. =>')
name = input('이름을 입력하세요. =>')

kor_grade = int(input('국어 점수를 입력하세요. => '))
eng_grade = int(input('영어 점수를 입력하세요. => '))
math_grade = int(input('수학 점수를 입력하세요. => '))

total = kor_grade + eng_grade + math_grade

avg = total / 3

print('\n\t\t\t\t\t --- 성적표 ---')

print('--------------------------------------------------------------------')

print('  학번        이름       국어     영어    수학    총점     평균')

print('--------------------------------------------------------------------')

print('%4s     %3s     %3d     %3d     %3d     %3d     %5.2f' %
      (id, name, kor_grade, eng_grade, math_grade, total, avg))