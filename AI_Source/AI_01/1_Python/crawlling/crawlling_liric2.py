from bs4 import BeautifulSoup

xml_doc = """
<rss>
    <channel>
        <my>
            <song album="a1">
                <title>Song 1</title>
                <length>02:50</length>
            </song>
            <song album="a2">
                <title>Song 1</title>
                <length>04:10</length>
            </song>
            <song album="a3">
                <title>Song 3</title>
                <length>03:25</length>
            </song>
        </my>
    </channel>
</rss>
"""

soup = BeautifulSoup(xml_doc, 'html.parser')

print(soup.prettify())
# <rss>
#  <channel>
#   <my>
#    <song album="a1">
#     <title>
#      Song 1
#     </title>
#     <length>
#      02:50
#     </length>
#    </song>
#    <song album="a2">
#     <title>
#      Song 1
#     </title>
#     <length>
#      04:10
#     </length>
#    </song>
#    <song album="a3">
#     <title>
#      Song 3
#     </title>
#     <length>
#      03:25
#     </length>
#    </song>
#   </my>
#  </channel>
# </rss>

print('----------------------------------')

for song in soup.findAll('song'):
    print(song['album'])
    print(song.title.string)
    print(song.length.string)
    print()
# a1
# Song 1
# 02:50
# 
# a2
# Song 1
# 04:10
# 
# a3
# Song 3
# 03:25