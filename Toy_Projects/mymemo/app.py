# import requests
# from bs4 import BeautifulSoup
#
# url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=171539'
#
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get(url,headers=headers)
#
# soup = BeautifulSoup(data.text, 'html.parser')
#
# # 여기에 코딩을 해서 meta tag를 먼저 가져와보겠습니다.
# ogtitle = soup.select_one('meta[property="og:title"]')['content']
# ogimage = soup.select_one('meta[property="og:image"]')['content']
# ogdesc = soup.select_one('meta[property="og:description"]')['content']
# print(ogtitle,ogimage,ogdesc)


from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbpractice

## HTML을 주는 부분
@app.route('/')
def home():
   return render_template('index.html')


## API 역할을 하는 부분
@app.route('/memo', methods=['GET'])
def listing():
    memo_list = list(db.memo.find({},{'_id':False}))
    return jsonify({'memo':memo_list})


@app.route('/memo', methods=['POST'])
def saving():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    # 크롤링 코드
    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    # Meta Tag Data 가져오기
    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']

    doc = {'title':title,
           'image':image,
           'desc':desc,
           'url':url_receive,
           'comment':comment_receive}

    db.memo.insert_one(doc)
    return jsonify({'msg': '저장되었습니다.'})

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)