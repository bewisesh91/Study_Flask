from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.DB_WetimeTF


### 시작 페이지 ###
@app.route('/')
def wetimeTest():
    return render_template('login.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)