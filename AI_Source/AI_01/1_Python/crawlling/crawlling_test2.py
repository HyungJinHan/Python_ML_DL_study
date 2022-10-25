from bs4 import BeautifulSoup
import urllib.request as MyUrl

jURL = 'https://sports.donga.com/NewsStand/article/all/20220921/115561993/1'
response = MyUrl.urlopen(jURL)
soup = BeautifulSoup(response, 'html.parser')
print(soup.prettify())
print('---------------------------------------------------------')
for item in soup.findAll('item'):
    print('title :', item.title.string)
    print('description :', item.description.string)
    print('pubdate :', item.pubdate.string)
    print('script :', item.script.string)
    print('---------------------------------------------------------')