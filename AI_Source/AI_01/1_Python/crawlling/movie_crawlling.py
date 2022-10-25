# https://movie.naver.com/movie/sdb/rank/rmovie.naver
# ?sel=cnt(조회) / cur(평점 현재) / pnt(평점 모든)
# &tg=0
# &date=20220920
# &page=2
# name='div', attrs={'class': 'tit3'}

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pymysql
import csv

def menu_func():
    print(' ----메뉴----')
    print('1. 조회순 랭킹 조회')
    print('2. 현재 상영 영화 평점순 랭킹 조회')
    print('3. 모든 영화 평점순 랭킹 조회')
    print('6. 프로그램 종료')

def get_view_rank(searchDay, movies, movieRank):
    base = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
    parameter = '?sel=cnt' + ('&date=%d' % int(searchDay))
    url = urlopen(base + parameter)
    soup = BeautifulSoup(url, 'html.parser', from_encoding='utf8')
    try:
        for link in soup.findAll(name='div', attrs={'class': 'tit3'}):
            try:
                movie = link.find('a').text
                movies.append(movie)
                movieRank += 1
            except AttributeError as viewError:
                movie = 'N/A'
                movies.append(movie)
                movieRank += 1
    except AttributeError as e:
        print(searchDay + '해당 날짜의 데이터가 존재하지 않습니다.')

def get_current_rank(searchDay, movies, movieRank, scores, scoreRank):
    base = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
    parameter = '?sel=cur' + ('&date=%d' % int(searchDay))
    url = urlopen(base + parameter)
    soup = BeautifulSoup(url, 'html.parser', from_encoding='utf8')
    try:
        for link1 in soup.findAll(name='div', attrs={'class': 'tit5'}):
            try:
                movie = link1.find('a').text
                movies.append(movie)
                movieRank += 1
            except AttributeError as viewError:
                movie = 'N/A'
                movies.append(movie)
                movieRank += 1

        for link2 in soup.findAll(name='td', attrs={'class': 'point'}):
            try:
                score = link2.text
                scores.append(score)
                scoreRank += 1
            except AttributeError as scoreError:
                score = 'N/A'
                scores.append(score)
                scoreRank += 1
    except AttributeError as e:
        print(searchDay + '해당 날짜의 데이터가 존재하지 않습니다.')

def get_all_rank(searchDay, movies, movieRank, scores, scoreRank, startPage, endPage):
    for i in range(int(startPage), int(endPage) + 1):
        base = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver'
        parameter = '?sel=pnt' + ('&date=%d' % int(searchDay)) + ('&page=%d' % (int(i)))
        url = urlopen(base + parameter)
        soup = BeautifulSoup(url, 'html.parser', from_encoding='utf8')
        try:
            for link1 in soup.findAll(name='div', attrs={'class': 'tit5'}):
                try:
                    movie = link1.find('a').text
                    movies.append(movie)
                    movieRank += 1
                except AttributeError as viewError:
                    movie = 'N/A'
                    movies.append(movie)
                    movieRank += 1

            for link2 in soup.findAll(name='td', attrs={'class': 'point'}):
                try:
                    score = link2.text
                    scores.append(score)
                    scoreRank += 1
                except AttributeError as scoreError:
                    score = 'N/A'
                    scores.append(score)
                    scoreRank += 1
        except AttributeError as e:
            print(searchDay + '해당 날짜의 데이터가 존재하지 않습니다.')

def set_view_csv(searchDay, movies):
    f = open('movie_view_chart_%s.csv' % (searchDay),
             'wt',
             encoding='utf-8',
             newline='')
    wr = csv.writer(f,
                    delimiter=',',
                    quotechar='"',
                    quoting=csv.QUOTE_ALL)
    for i in range(len(movies)):
        wr.writerow((searchDay,
                     str(i + 1),
                     movies[i]))
    f.close()
    print('조회순으로 csv 파일 저장을 완료했습니다.')

def set_score_csv(searchDay, movies, scores):
    f = open('movie_score_chart_%s.csv' % (searchDay),
             'wt',
             encoding='utf-8',
             newline='')
    wr = csv.writer(f,
                    delimiter=',',
                    quotechar='"',
                    quoting=csv.QUOTE_ALL)
    for i in range(len(movies)):
        wr.writerow((searchDay,
                     str(i + 1),
                     movies[i],
                     scores[i]))
    f.close()
    print('현재 개봉한 영화의 평점순으로 csv 파일 저장을 완료했습니다.')

def set_all_csv(searchDay, movies, scores, startPage, endPage):
    f = open('movie_all_chart_%s.csv' % (searchDay),
             'wt',
             encoding='utf-8',
             newline='')
    wr = csv.writer(f,
                    delimiter=',',
                    quotechar='"',
                    quoting=csv.QUOTE_ALL)
    pageMovieRank = ((int(startPage) - 1) * 50) + 1
    for i in range(len(movies)):
        wr.writerow((searchDay,
                     str(pageMovieRank + i),
                     movies[i],
                     scores[i],
                     startPage,
                     endPage))
    f.close()
    print('모든 영화의 평점순으로 csv 파일 저장을 완료했습니다.')

def set_view_db(searchDay, movies):
    dbconn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='bbs',
        charset='utf8'
    )
    dbcursor = dbconn.cursor()
    dbcursor.execute('DROP TABLE IF EXISTS movies_view_chart')
    dbcursor.execute('''CREATE TABLE IF NOT EXISTS movies_view_chart (
                            search_day TEXT,
                            ranking INT PRIMARY KEY,
                            movie TEXT
                        )''')
    sql = 'INSERT INTO movies_view_chart(search_day, ranking, movie) VALUES (%s, %s, %s)'

    for i in range(len(movies)):
        try:
            dbcursor.execute(sql, (searchDay, i, movies[i]))
        except:
            print('MySql Error')

    print('데이터베이스에 저장이 완료되었습니다.')
    dbcursor.execute('SELECT * FROM movies_view_chart')
    res = dbcursor.fetchall()
    for row in res:
        print(str(row[0]) + '\t' + '\t' + '\t' + '\t' +
              str(row[1]) + '\t' + '\t' + '\t' + '\t' +
              str(row[2]) + '\t' + '\t' + '\t' + '\t')
    dbconn.commit()
    dbcursor.close()
    dbconn.close()

def set_score_db(searchDay, movies, scores):
    dbconn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='bbs',
        charset='utf8'
    )
    dbcursor = dbconn.cursor()
    dbcursor.execute('DROP TABLE IF EXISTS movies_score_chart')
    dbcursor.execute('''CREATE TABLE IF NOT EXISTS movies_score_chart (
                            search_day TEXT,
                            ranking INT PRIMARY KEY,
                            movie TEXT,
                            score TEXT
                        )''')
    sql = 'INSERT INTO movies_score_chart(search_day, ranking, movie, score) VALUES (%s, %s, %s, %s)'

    for i in range(len(movies)):
        try:
            dbcursor.execute(sql, (searchDay, i + 1, movies[i], scores[i]))
        except:
            print('MySql Error')

    dbcursor.execute('SELECT * FROM movies_score_chart')
    res = dbcursor.fetchall()
    for row in res:
        print(str(row[0]) + '\t' + '\t' + '\t' + '\t' +
              str(row[1]) + '\t' + '\t' + '\t' + '\t' +
              str(row[2]) + '\t' + '\t' + '\t' + '\t' +
              str(row[3]) + '\t' + '\t' + '\t' + '\t')
    print('데이터베이스에 저장이 완료되었습니다.')
    dbconn.commit()
    dbcursor.close()
    dbconn.close()

def set_all_db(searchDay, movies, scores, startPage, endPage):
    dbconn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='bbs',
        charset='utf8'
    )
    dbcursor = dbconn.cursor()
    dbcursor.execute('DROP TABLE IF EXISTS movies_all_chart')
    dbcursor.execute('''CREATE TABLE IF NOT EXISTS movies_all_chart (
                            search_day TEXT,
                            ranking INT PRIMARY KEY,
                            movie TEXT,
                            score TEXT,
                            start_page TEXT,
                            end_page TEXT
                        )''')
    sql = 'INSERT INTO movies_all_chart(search_day, ranking, movie, score, start_page, end_page) VALUES (%s, %s, %s, %s, %s, %s)'
    pageMovieRank = ((int(startPage) - 1) * 50) + 1
    for i in range(len(movies)):
        try:
            dbcursor.execute(sql, (searchDay, pageMovieRank + i, movies[i], scores[i], startPage, endPage))
        except:
            print('MySql Error')

    dbcursor.execute('SELECT * FROM movies_all_chart')
    res = dbcursor.fetchall()
    for row in res:
        print(str(row[0]) + '\t' + '\t' + '\t' + '\t' +
              str(row[1]) + '\t' + '\t' + '\t' + '\t' +
              str(row[2]) + '\t' + '\t' + '\t' + '\t' +
              str(row[3]) + '\t' + '\t' + '\t' + '\t' +
              str(row[4]) + '\t' + '\t' + '\t' + '\t')
    print('데이터베이스에 저장이 완료되었습니다.')
    dbconn.commit()
    dbcursor.close()
    dbconn.close()

if __name__ == '__main__':
    movies = []
    scores = []
    movieRank = 0
    scoreRank = 0
    while True:
        menu_func()
        menu_select = int(input('메뉴를 선택하세요. : '))
        if menu_select == 1:
            while True:
                try:
                    searchDay = input('검색할 영화 랭킹의 날짜 8자리를 입력해주세요. (ex : 20220921) : ')
                    if len(searchDay) > 8 or len(searchDay) < 8:
                        print('\n날짜는 8자리로만 입력해주세요.')
                        continue
                    else:
                        break
                except:
                    print('\n날짜는 8자리의 숫자로만 입력해주세요.')
                    continue
                else:
                    break
            get_view_rank(searchDay, movies, movieRank)
            set_view_db(searchDay, movies)
            set_view_csv(searchDay, movies)
            # print(movies)
        elif menu_select == 2:
            while True:
                try:
                    searchDay = input('검색할 영화 랭킹의 날짜 8자리를 입력해주세요. (ex : 20220921) : ')
                    if len(searchDay) > 8 or len(searchDay) < 8:
                        print('\n날짜는 8자리로만 입력해주세요.')
                        continue
                    else:
                        break
                except:
                    print('\n날짜는 8자리의 숫자로만 입력해주세요.')
                    continue
                else:
                    break
            get_current_rank(searchDay, movies, movieRank, scores, scoreRank)
            set_score_db(searchDay, movies, scores)
            set_score_csv(searchDay, movies, scores)
            # print(movies, scores)
        elif menu_select == 3:
            while True:
                try:
                    searchDay = input('검색할 영화 랭킹의 날짜 8자리를 입력해주세요. (ex : 20220921) : ')
                    if len(searchDay) > 8 or len(searchDay) < 8:
                        print('\n날짜는 8자리로만 입력해주세요.')
                        continue
                    else:
                        break
                except:
                    print('\n날짜는 8자리의 숫자로만 입력해주세요.')
                    continue
                else:
                    break
            while True:
                try:
                    startPage = int(input('시작 페이지를 선택하세요. : '))
                    if startPage > 40:
                        print('\n페이지의 수는 최대 40 페이지 입니다.')
                        continue
                    else:
                        break
                except:
                    print('\n시작 페이지는 숫자로 입력해주세요.')
                    continue
                else:
                    break
            while True:
                try:
                    endPage = int(input('끝 페이지를 선택하세요. : '))
                    if endPage > 40:
                        print('\n페이지의 수는 최대 40 페이지 입니다.')
                        continue
                    else:
                        break
                except:
                    print('\n끝 페이지는 숫자로 입력해주세요.')
                    continue
                else:
                    break
            get_all_rank(searchDay, movies, movieRank, scores, scoreRank, startPage, endPage)
            set_all_csv(searchDay, movies, scores, startPage, endPage)
            set_all_db(searchDay, movies, scores, startPage, endPage)
            # print(movies, scores, startPage, endPage)
        elif menu_select == 6:
            print('\n프로그램을 종료합니다.')
            break
        else:
            print('\n메뉴를 다시 선택해 주세요.')