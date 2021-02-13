import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient

# local에서 DB를 만드는 과정이다.
client = MongoClient('localhost', 27017)
db = client.dbpractice

# 스크래핑 방지를 우회하기 위한 방법이다.
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

# 스크래핑을 진행할 사이트의 주소를 입력한다.
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200303', headers=headers)

# 스크래핑한 데이터에서 텍스트만을 뽑아서 html로 만들어준다.
soup = BeautifulSoup(data.text, 'html.parser')

# 코딩 시작

title = soup.select_one('#old_content > table > tbody > tr:nth-child(2) > td.title > div > a')
print(title)
print(title.text) # 텍스트를 가져온다.
print(title['href']) # href에 해당하는 속성 값을 가져온다.

### selector 이해하기 ###
    # 그린 북
    # #old_content > table > tbody > tr:nth-child(2)
    # 가버나움
    # #old_content > table > tbody > tr:nth-child(3)
# 두 selector 간 차이가 나는 것은 child( )안의 숫자
# 따라서, #old_content > table > tbody > tr 까지만 select 해주면 전체 영화 정보를 담을 수 있다.

movies = soup.select('#old_content > table > tbody > tr')
for movie in movies :
    print(movie)

# 영화의 제목들은 다음 selector에 담겨 있다.
# #old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# tr 다음의 td.title > div > a 만 사용하여 영화 제목들을 선택한다.

movies = soup.select('#old_content > table > tbody > tr')
for movie in movies :
    title = movie.select_one('td.title > div > a')
    print(title)

# 그런데 중간 중간 None이라는 결과가 포함되어 있다.
# 해당 결과를 제외하기 위해서 조건을 적용한다.
movies = soup.select('#old_content > table > tbody > tr')
for movie in movies :
    title = movie.select_one('td.title > div > a')
    if title is not None :
        print(title)
        print(title.text)

# 영화의 랭크, 제목, 평점을 정리하면 아래와 같다.
movies = soup.select('#old_content > table > tbody > tr')
for movie in movies :
    rank = movie.select_one('td:nth-child(1) > img')
    title = movie.select_one('td.title > div > a')
    score = movie.select_one('td.point')
    if title is not None :
        print(rank)
        print(rank['alt'])
        print(title)
        print(title.text)
        print(score)
        print(score.text)

movies = soup.select('#old_content > table > tbody > tr')
for movie in movies :
    title = movie.select_one('td.title > div > a')
    if title is not None:
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        title = movie.select_one('td.title > div > a').text
        score = movie.select_one('td.point').text
        print(rank, title, score)


# 영화 정보를 DB에 저장하기
# movies = soup.select('#old_content > table > tbody > tr')
# for movie in movies:
#     title = movie.select_one('td.title > div > a')
#     if title is not None:
#         rank = movie.select_one('td:nth-child(1) > img')['alt']
#         title = movie.select_one('td.title > div > a').text
#         score = movie.select_one('td.point').text
#         doc = {'rank':rank,
#                'title':title,
#                'score':score
#                }
#         db.movies.insert_one(doc)

# 중요한 것은, DB에 저장되는 데이터의 타입이다. 정확하게 입력하지 않으면 오류가 발생할 수 있다.
