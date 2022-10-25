from bs4 import BeautifulSoup

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link3">
#     Tillie
#    </a>
#    ;
# and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>

print('----------soup.title----------')
print(soup.title)
# <title>The Dormouse's story</title>
print()

print('----------soup.title.name----------')
print(soup.title.name)
# title
print()

print('----------soup.title.string----------')
print(soup.title.string)
# The Dormouse's story
print()

print('----------soup.title.parent.name----------')
print(soup.title.parent.name)
# head
print()

print('----------soup.p----------')
print(soup.p)
# <p class="title"><b>The Dormouse's story</b></p>
print()

print('----------soup.p["class"]----------')
print(soup.p['class'])
# ['title']
print()

print('----------soup.find(class_="title")----------')
print(soup.find(class_='title'))
print()

print('----------soup.a----------')
print(soup.a)
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
print()

print('----------soup.a["class"]----------')
print(soup.a['class'])
# ['sister']
print()

print('----------soup.findAll("a")----------')
print(soup.findAll('a'))
# = print(soup.find_all('a'))
# [
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# ]
print()

print('----------soup.find(id="link1")----------')
print(soup.find(id='link1'))
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>