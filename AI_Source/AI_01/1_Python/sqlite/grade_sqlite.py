from grade_sqlite_class import Grade
import sqlite3

def menu_func():
    print(' ----메뉴----')
    print('1. 성적정보 입력')
    print('2. 성적정보 확인')
    print('3. 성적정보 조회')
    print('4. 성적정보 수정')
    print('5. 성적정보 삭제')
    print('6. 프로그램 종료')

def input_func():
    obj = Grade()
    obj.setInfo()
    obj.setSum()
    obj.setAvg()
    obj.setGrade()
    # sql = "INSERT INTO grade (id, name, kor, eng, math, sum, avg, grade) values (?, ?, ?, ?, ?, ?, ?, ?)"
    # dbconn = sqlite3.connect('grade.db')
    # dbcursor = dbconn.cursor()
    # try:
    #     dbcursor.execute(sql, (obj.id, obj.name, obj.kor, obj.eng, obj.math, obj.sum, obj.avg, obj.grade))
    # except:
    #     dbconn.commit()
    # finally:
    #     dbcursor.close()
    #     dbconn.close()
    print('-----------------------------------------------------------------------------')

def output_func():
    total_avg = 0
    dbconn = sqlite3.connect('grade.db')
    dbcursor = dbconn.cursor()
    dbcursor.execute('SELECT * FROM grade')
    res = dbcursor.fetchall()
    for row in res:
        total_avg += row[6]
    obj = Grade()
    obj.print_board()
    obj.result_print()
    print('-----------------------------------------------------------------------------')
    print('학생 수 : %d / 학생 평균 : %.2f' % (len(res), total_avg / len(res)))
    print('성적 데이터 출력이 종료됩니다.\n')

def show_func():
    dbconn = sqlite3.connect('grade.db')
    dbcursor = dbconn.cursor()
    id_select = input('성적을 조회할 학번을 입력하세요. : ')
    dbcursor.execute('SELECT * FROM grade')
    res = dbcursor.fetchall()
    for row in res:
        if id_select == row[0]:
            print('-----------------------------------------------------------------------------')
            print(str(row[0]) + '\t' + '\t' +
                  str(row[1]) + '\t' + '\t' +
                  str(row[2]) + '\t' + '\t' +
                  str(row[3]) + '\t' + '\t' +
                  str(row[4]) + '\t' + '\t' +
                  str(row[5]) + '\t' + '\t' +
                  str(row[6]) + '\t' + '\t' +
                  str(row[7]) + '\t' + '\t')
            print('\n해당 학번의 정보를 조회합니다.')
            dbcursor.close()
            dbconn.close()
            break
    else:
        print('\n성적을 조회할 학번이 없습니다.')

def update_func():
    dbconn = sqlite3.connect('grade.db')
    dbcursor = dbconn.cursor()
    id_select = input('성적을 수정할 학번을 입력하세요. : ')
    dbcursor.execute('SELECT * FROM grade')
    res = dbcursor.fetchall()
    for row in res:
        if id_select == row[0]:
            while True:
                try:
                    kor = int(input('국어 점수를 입력하세요. => '))
                    if kor > 100:
                        print('\n수정할 점수는 100점 이하로 입력해주세요.')
                        continue
                    else:
                        break
                except:
                    print('\n수정할 점수는 숫자로만 입력해주세요.')
                    continue
                else:
                    break
            while True:
                try:
                    eng = int(input('영어 점수를 입력하세요. => '))
                    if eng > 100:
                        print('\n수정할 점수는 100점 이하로 입력해주세요.')
                        continue
                    else:
                        break
                except:
                    print('\n수정할 점수는 숫자로만 입력해주세요.')
                    continue
                else:
                    break
            while True:
                try:
                    math = int(input('수학 점수를 입력하세요. => '))
                    if math > 100:
                        print('\n수정할 점수는 100점 이하로 입력해주세요.')
                        continue
                    else:
                        break
                except:
                    print('\n수정할 점수는 숫자로만 입력해주세요.')
                    continue
                else:
                    break
            sum_up = kor + eng + math
            avg = sum_up / 3
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
            dbcursor.execute('UPDATE grade SET kor = ?, eng = ?, math = ?, sum = ?, avg = ?, grade =? WHERE id = ?',
                             (kor, eng, math, sum_up, avg, grade, id_select))
            dbconn.commit()
            dbcursor.close()
            dbconn.close()
            print('\n해당 학번의 정보가 수정되었습니다.')
            break
    else:
        print('\n성적을 수정할 학번이 없습니다.')

def delete_func():
    dbconn = sqlite3.connect('grade.db')
    dbcursor = dbconn.cursor()
    id_select = input('성적을 삭제할 학번을 입력하세요. : ')
    dbcursor.execute('SELECT * FROM grade')
    res = dbcursor.fetchall()
    for row in res:
        if id_select == row[0]:
            dbcursor.execute('DELETE FROM grade WHERE id = ?', (id_select,))
            dbconn.commit()
            print('\n해당 학번의 정보가 삭제되었습니다.')
            break
    else:
        print('\n성적을 삭제할 학번이 없습니다.')

if __name__ == '__main__':
    while True:
        menu_func()
        try:
            menu_select = int(input('메뉴를 선택하세요. : '))
        except:
            print('메뉴 선택은 숫자만 가능합니다.\n')
            continue
        if menu_select == 1:
            input_func()
        elif menu_select == 2:
            output_func()
        elif menu_select == 3:
            show_func()
        elif menu_select == 4:
            update_func()
        elif menu_select == 5:
            delete_func()
        elif menu_select == 6:
            print('\n프로그램을 종료합니다.')
            break
        else:
            print('\n메뉴를 다시 선택해 주세요.\n')