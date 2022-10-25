import os
import sys
import json
import urllib.request

client_id = "SPW_iLqHpIeAA3MQiJHH"
client_secret = "KMQWDX_p6k"

encText = urllib.parse.quote(input('검색할 단어를 입력해주세요. => '))
encDisplay = "&display=" + input('검색 결과를 표시할 수를 입력해주세요. => ')
encSort = "&sort=" + 'sim'
url = "https://openapi.naver.com/v1/search/blog?query=" + encText + encDisplay + encSort # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)

rescode = response.getcode()

if(rescode==200):
    response_body = json.loads(response.read().decode('utf-8'))['items']
    lastResult = json.dumps(response_body, indent=4)
    fp = open(
        input(
            '저장할 파일의 제목을 적어주세요. => ') + '.json',
        'wt'
    )
    # response_items = result['items']
    fp.write(lastResult)
    print(lastResult)
    fp.close()
    print('파일이 저장되었습니다.')
else:
    print("Error Code:" + rescode)

# "title":"
# "link"
# "bloggername"