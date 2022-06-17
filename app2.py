from flask import Flask, jsonify
from http import HTTPStatus

app = Flask(__name__)

@app.route('/hithere', methods=['GET'])
        # 주소뒤에 이 경로를
        # 넣어줘야 한다
def hi_there() :
    return 'Hi there~~~'

@app.route('/add', methods=['GET'])
def add() :
    data = 283 + 111
    return str(data)

@app.route('/', methods=['GET'])
def root():
    return '안녕하세요'

@app.route('/act/data', methods = ['GET'])
def act():
    ret = {'count' : 2, 
            'students':[{'name' : '홍길동', 'age' : 30} ,
                        {'name' : '김나나', 'age' : 25}]
            }
    return jsonify(ret)

if __name__ == '__main__' :
    app.run()