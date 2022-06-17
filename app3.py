from flask import Flask, jsonify, request
from http import HTTPStatus

app = Flask(__name__)

                                # 웹 브라우저는 get으로만 요청해서 실행안됨
                                # 그래서 postman 설치해서사용
@app.route('/add_two_nums', methods = ['POST'])
def add() :
    # 클라이언트로부터 두 수를 받는다.
    data = request.get_json()
    ret = data['X'] + data['y']
    result = {'result' : ret}

    return jsonify(result)

if __name__ == '__main__' :
    app.run()
#   app.run(port= 5001)