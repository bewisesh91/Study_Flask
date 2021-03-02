from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests


app = Flask(__name__)

client = MongoClient('52.79.227.172', 27017, username="test", password="test")
db = client.dbsparta_plus_week2


@app.route('/')
def main():
    # DB에서 저장된 단어 찾아서 HTML에 나타내기
    words = list(db.words.find({}, {'_id': False}))

    # 입력된 단어가 이상할 경우
    msg = request.args.get('msg')
    return render_template("index.html", words=words, msg=msg)


@app.route('/detail/<keyword>')
def detail(keyword):
    # 단어 저장 / 삭제 버튼 변경하기
    # ajax를 따로 작성해주는 것이 아니라, 도메인에 ?status_give 항목을 넣어주면 된다.
    status_receive = request.args.get('status_give')

    # API에서 단어 뜻 찾아서 결과 보내기
    r = requests.get(f"https://owlbot.info/api/v4/dictionary/{keyword}", headers={"Authorization": "Token 03aaf49135489d637d083b3c2275c272e9d10f81"})

    if r.status_code != 200: # keyword가 정상적이지 않을 경우
       return redirect(url_for('main', msg= '정확한 단어를 입력해주세요.')) # main 함수에 해당하는 url로 가

    result = r.json() # 사전 API에서 얻은 값
    print(result)

    return render_template("detail.html", word=keyword, result=result, status=status_receive)

@app.route('/api/save_word', methods=['POST'])
def save_word():
    # 단어 저장하기
    word_receive = request.form['word_give']
    definition_receive = request.form['definition_give']
    doc = {
        'word': word_receive,
        'definition': definition_receive
    }
    db.words.insert_one(doc)

    return jsonify({'result': 'success', 'msg': f'{word_receive} 저장'})


@app.route('/api/delete_word', methods=['POST'])
def delete_word():
    # 단어 삭제하기
    word_receive = request.form['word_give']
    db.words.delete_one({'word': word_receive})
    return jsonify({'result': 'success', 'msg': f'{word_receive} 삭제'})


@app.route('/api/save_ex', methods=['POST'])
def save_ex():
    # 예문 저장하기
    word_receive = request.form['word_give']
    example_receive = request.form['example_give']
    doc = {
        'word': word_receive,
        'example': example_receive
    }
    db.examples.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/api/get_exs', methods=['GET'])
def get_exs():
    # 예문 가져오기
    word_receive = request.args.get('word_give')
    result = list(db.examples.find({'word': word_receive}, {'_id': False}))
    print(result)
    return jsonify({'result': 'success', 'examples': result})


@app.route('/api/delete_ex', methods=['POST'])
def delete_ex():
    # 예문 삭제하기
    word_receive = request.form['word_give']
    number_receive = int(request.form['number_give'])
    example = list(db.examples.find({'word': word_receive}))[number_receive]['example']
    db.examples.delete_one({'word':word_receive, 'example': example})
    return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)