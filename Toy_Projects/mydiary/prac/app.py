from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/')
def main():
    username = "Leo.myfavorite"
    return render_template("index.html", name = username)


@app.route('/detail/<keyword>')
def detail(keyword):
    # r = requests.get('http://openapi.seoul.go.kr:8088/6d4d776b466c656533356a4b4b5872/json/RealtimeCityAir/1/99')
    # response = r.json()
    # rows = response['RealtimeCityAir']['row']

    r = requests.get(f"https://owlbot.info/api/v4/dictionary/{keyword}", headers={"Authorization": "Token 03aaf49135489d637d083b3c2275c272e9d10f81"})
    result = r.json()
    print(result)

    # ajax 사용 시
    # word_receive = request.args.get('word_give')
    # print(word_receive)
    return render_template("detail.html", word = keyword)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)