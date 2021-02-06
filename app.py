from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 수강 신청하기(POST) API
@app.route('/apply', methods=['POST'])
def apply():
    name_receive = request.form['name_give']
    order_receive = request.form['order_give']
    email_receive = request.form['email_give']
    phone_receive = request.form['phone_give']

    doc = {'name':name_receive, 'order':order_receive, 'email':email_receive, 'phone':phone_receive}
    db.orderlist.insert_one(doc)

    return jsonify({'msg': '수강 신청 되었습니다.'})


# 수강 신청 목록보기(Read) API
@app.route('/applylist', methods=['GET'])
def view_applys():
    all_applies = list(db.orderlist.find({}, {'_id': False}))
    return jsonify({'applies': all_applies})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)