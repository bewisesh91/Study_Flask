from flask import Flask, render_template, request, jsonify, redirect, url_for
from pymongo import MongoClient
import requests


app = Flask(__name__)

client = MongoClient('52.79.227.172', 27017, username="test", password="test")
db = client.mydict


@app.route('/', methods=['GET'])
def main():
    words = list(db.words.find({}, {'_id': False}))
    print(words)
    return render_template('index.html', words=words)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)