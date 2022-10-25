fp = open('text.txt', 'wt', encoding='utf-8')
fp.write('%d\n' % int(input('정수를 입력하세요. => ')))
fp.write('%.2f\n' % float(input('실수를 입력하세요. => ')))
fp.write('%s\n' % input('원하는 문구를 입력하세요. => '))
fp.write('%s\n' % input('원하는 문구를 입력하세요. => '))
fp.write('%s\n' % '--------------------------------------')
fp.write('%s\n' % '입력을 종료합니다.')
fp.close()

fp = open('text.txt', 'rt', encoding='utf-8')
contents = fp.read()
print(contents)
fp.close()
# close는 open한 파일을 처리한 후 종료됨
# input에 입력한 결과들을 출력함

fp = open('text.txt', 'rt', encoding='utf-8')
line = fp.readline()
print(line.strip())
line = fp.readline()
print(line.strip())
line = fp.readline()
print(line.strip())
line = fp.readline()
print(line.strip())
line = fp.readline()
print(line.strip())
line = fp.readline()
print(line.strip())
fp.close()
# 한 줄씩 읽어줌 (줄 바꿈을 기준으로)

fp = open('text.txt', 'rt', encoding='utf-8')
while True:
    line = fp.readline()
    if line == '':
        break
    print(line.strip())
fp.close()
# readline을 반복문 처리해서 리팩토링

fp = open('text.txt', 'rt', encoding='utf-8')
lines = fp.readlines()
print(lines)
fp.close()
# ['입력한\n', '값이\n', 'list\n', '형식으로\n', '출력']

fp = open('text.txt', 'rt', encoding='utf-8')
line = fp.readlines()
for line in lines:
    print(line, end='')
fp.close()
# 입력한
# 값을
# 반복문으로
# 출력해서
# 뽑아내기

with open('text.txt', 'rt', encoding='utf-8') as fp:
    with_read = fp.read()
print(with_read)