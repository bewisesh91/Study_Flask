from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)


# client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://leo:leo@localhost', 27017)
db = client.DB_WetimeTF


# 시작 페이지 #
@app.route('/')
def home():
    return render_template('index.html')


########### 추가 한 부분 ###########
@app.route('/result')
def result():
    return render_template('result.html')
########### 추가 한 부분 ###########


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
