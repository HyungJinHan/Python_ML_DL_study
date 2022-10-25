import json
import urllib.request

client_id = "SPW_iLqHpIeAA3MQiJHH"
client_secret = "KMQWDX_p6k"

# encText = urllib.parse.quote(input('검색할 단어를 입력해주세요. => '))
# encDisplay = "&display=" + input('검색 결과를 표시할 수를 입력해주세요. => ')
# encSort = "&sort=" + 'sim'
# url = "https://openapi.naver.com/v1/search/blog?query=" + encText + encDisplay + encSort # JSON 결과
# # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과

encText = urllib.parse.quote(input('검색할 단어를 입력해주세요. => '))
encDisplay = int(input('검색 결과를 표시할 수를 입력해주세요. => '))
encStart = int(input('검색 결과의 시작 지점을 숫자로 입력해주세요. => '))
encSort = 'sim'
url = "https://openapi.naver.com/v1/search/blog?query=%s&display=%d&start=%d&sort=%s" \
      % (encText, encDisplay, encStart, encSort) # JSON 결과

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id", client_id)
request.add_header("X-Naver-Client-Secret", client_secret)

response = urllib.request.urlopen(request)

rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    response_decode = response_body.decode('utf-8')
    response_json = json.loads(response_decode)['items']
    response_dumps = json.dumps(
        response_json,
        indent=4,
        ensure_ascii=False
    )
    fp = open(
        input('저장할 파일의 제목을 적어주세요. => ')
        + '.json',
        'wt',
        encoding='utf-8'
    )
    fp.write(response_dumps)
    fp.close()
    print(response_dumps)
    print('파일이 저장되었습니다.')
else:
    print("Error Code:" + rescode)

# "title":"
# "link"
# "bloggername"