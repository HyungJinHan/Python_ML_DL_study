lst = []

id = input('학번을 입력하세요. =>')
name = input('이름을 입력하세요. =>')

kor_grade = int(input('국어 점수를 입력하세요. => '))
eng_grade = int(input('영어 점수를 입력하세요. => '))
math_grade = int(input('수학 점수를 입력하세요. => '))

lst.append(id)
lst.append(name)
lst.append(kor_grade)
lst.append(eng_grade)
lst.append(math_grade)

lst.append(lst[2] + lst[3] + lst[4])

lst.append(lst[5] / 3)

print(lst)

print('\n\t\t\t\t\t --- 성적표 ---')

print('--------------------------------------------------------------------')

print('  학번         이름      국어     영어     수학    총점     평균')

print('--------------------------------------------------------------------')

print('%4s     %3s     %3d     %3d     %3d     %3d     %5.2f' %
      (lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6]))