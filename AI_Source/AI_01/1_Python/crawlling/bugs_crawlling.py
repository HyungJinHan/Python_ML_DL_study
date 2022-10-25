from bs4 import BeautifulSoup
from urllib.request import urlopen
import pymysql
import csv

def get_search_result(searchDay, artists, artistRank, titles, titleRank):
    base = 'https://music.bugs.co.kr/chart/track/day/total'
    parameter = '?chartdate=%d' % int(searchDay)
    url = urlopen(base + parameter)
    soup = BeautifulSoup(url, 'html.parser', from_encoding='utf8')
    try:
        for link1 in soup.findAll(name='p', attrs={'class': 'artist'}):
            try:
                artist = link1.find('a').text
                artists.append(artist)
                artistRank += 1
            except AttributeError as artistError:
                artist = 'N/A'
                artists.append(artist)
                artistRank += 1

        for link2 in soup.findAll(name='p', attrs={'class': 'title'}):
            try:
                title = link2.find('a').text
                titles.append(title)
                titleRank += 1
            except AttributeError as titleError:
                title = 'N/A'
                titles.append(title)
                titleRank += 1
    except AttributeError as e:
        print(searchDay + '해당 날짜의 데이터가 존재하지 않습니다.')
    except IndexError as index:
        print('IndexError / ' + '아티스트 리스트 길이 : ' + str(len(artists))
              + ' / 곡 리스트 길이 : ' + str(len(titles)))

def set_data_csv(searchDay, artists, titles):
    f = open('bugschart_%s.csv' % (searchDay),
             'wt',
             encoding='utf-8',
             newline='')
    wr = csv.writer(f,
                    delimiter=',',
                    quotechar='"',
                    quoting=csv.QUOTE_ALL)
    for i in range(0, 100):
        wr.writerow((searchDay,
                     str(i + 1),
                     artists[i],
                     titles[i]))
    f.close()

def set_sata_db(searchDay, artists, titles):
    dbconn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='bbs',
        charset='utf8'
    )
    dbcursor = dbconn.cursor()
    dbcursor.execute('DROP TABLE IF EXISTS bugs_chart')
    dbcursor.execute('''CREATE TABLE IF NOT EXISTS bugs_chart (
                            search_day TEXT,
                            ranking INT PRIMARY KEY,
                            artist TEXT,
                            title TEXT
                        )''')
    sql = 'INSERT INTO bugs_chart(search_day, ranking, artist, title) VALUES (%s, %s, %s, %s)'

    for i in range(100):
        try:
            dbcursor.execute(sql, (searchDay, i + 1, artists[i], titles[i]))
        except:
            print('MySql Error')

    print('데이터베이스에 저장이 완료되었습니다.')
    dbconn.commit()
    dbcursor.close()
    dbconn.close()

if __name__ == '__main__':
    artists = []
    titles = []
    artistsRank = 0
    artistRank = 0
    titleRank = 0
    searchDay = input('검색할 차트의 날짜를 8자리로 입력해주세요. (ex : 20220921) => ')

    get_search_result(searchDay, artists, artistRank, titles, titleRank)
    set_data_csv(searchDay, artists, titles)
    set_sata_db(searchDay, artists, titles)