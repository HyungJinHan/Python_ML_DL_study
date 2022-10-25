import json
import urllib.request
import datetime
from secret_key import *
import csv
import pymysql
import re # 정규표현식 관련 모듈

def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print('[%s] Url Request Success' % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print('[%s] Bad Request : %s' % (datetime.datetime.now(), url))
        return None

def get_search_result(search_node, search_text, page_start, page_display):
    base = 'https://openapi.naver.com/v1/search/'
    node = '%s.json' % search_node
    parameters = '?query=%s&start=%d&display=%d' %\
                 (urllib.parse.quote(search_text), page_start, page_display)
    url = base + node + parameters
    request_data = get_request_url(url)
    if request_data == None:
        return None
    else:
        return json.loads(request_data)

def get_post_data(post, json_result):
    title = post['title']
    bloggername = post['bloggername']
    link = post['link']
    bloggerlink = post['bloggerlink']
    postdate = post['postdate']

    json_result.append(
        {
            'title': title,
            'bloggername': bloggername,
            'link': link,
            'bloggerlink': bloggerlink,
            'postdate': postdate
        }
    )
    return

def main():
    json_result = []

    search_node = 'blog'
    search_text = input('검색어를 입력해주세요. => ')
    page_start = int(input('검색 결과의 시작 지점을 숫자로 입력해주세요. => '))
    page_display = int(input('검색 결과를 표시할 수를 입력해주세요. => '))
    result_limit = int(input('검색 내용의 총 개수를 입력해주세요. => '))
    json_search = get_search_result(search_node, search_text, page_start, page_display)
    # print(json_search)

    while ((json_search != None) and (json_search['display'] != 0)):
        for post in json_search['items']:
            get_post_data(post, json_result)

        page_start_new = json_search['start'] + json_search['display']
        if (page_start_new > result_limit):
            break

        json_search = get_search_result(search_node, search_text, page_start_new, page_display)

    with open(
            '%s_naver_%s.json' % (search_text, search_node),
            'wt',
            encoding='utf-8'
    ) as outfile:
        result_all = json.dumps(
            json_result,
            indent=4,
            ensure_ascii=False
        )
        outfile.write(result_all)

    get_data_csv(json_result, search_text, search_node)
    print('%s_naver_%s.json Saved' % (search_text, search_node))
    set_data_db(json_result)

def get_data_csv(json_result, search_text, search_node):
    with open(
        '%s_naver_%s.csv' % (search_text, search_node),
        'wt',
        encoding='utf-8',
        newline=''
    ) as f:
        wr = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        wr.writerow(
            ('title',
             'bloggername',
             'link',
             'bloggerlink',
             'postdate')
        )
        for row in json_result:
            wr.writerow(
                (row['title'],
                 row['bloggername'],
                 row['link'],
                 row['bloggerlink'],
                 row['postdate'])
            )
    print('%s_naver_%s.csv Saved' % (search_text, search_node))
    # with 사용으로 close를 별도로 하지 않도록 작업

def set_data_db(json_result):
    dbconn = pymysql.connect(
        host='localhost',
        user='root',
        password='123456',
        db='bbs',
        charset='utf8'
    )
    dbcursor = dbconn.cursor()
    dbcursor.execute('DROP TABLE IF EXISTS naver_mysql')
    dbcursor.execute('''CREATE TABLE IF NOT EXISTS naver_mysql (
                        id INT AUTO_INCREMENT PRIMARY KEY,
                        title TEXT,
                        bloggername TEXT,
                        link TEXT,
                        bloggerlink TEXT,
                        postdate TEXT
                    )''')
    for row in json_result:
        try:
            dbcursor.execute(
                'INSERT INTO naver_mysql (title, bloggername, link, bloggerlink, postdate) VALUES (%s, %s, %s, %s, %s)',
                (row['title'], row['bloggername'], row['link'], row['bloggerlink'], row['postdate'])
            )
        except:
            for res in row:
                row[res] = re.sub('[^가-힝0-9a-zA-Z<>&.?:/#\[\]\\s]', ' ', row[res])

    dbcursor.execute('SELECT * FROM naver_mysql')
    res = dbcursor.fetchall()
    for row in res:
        print(str(row[0]) + '\t' + '\t' + '\t' + '\t' +
              str(row[1]) + '\t' + '\t' + '\t' + '\t' +
              str(row[2]) + '\t' + '\t' + '\t' + '\t' +
              str(row[3]) + '\t' + '\t' + '\t' + '\t' +
              str(row[4]) + '\t' + '\t' + '\t' + '\t')
    dbconn.commit()
    dbcursor.close()
    dbconn.close()

if __name__ == '__main__':
    main()