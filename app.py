from flask import Flask, request
# JWT 사용을 위한 SECRET_KEY 정보가 들어있는 파일 임포트
from config import Config
from flask.json import jsonify
from http import HTTPStatus

from flask_restful import Api

from flask_jwt_extended import JWTManager

from resources.register import UserRegisterResource


app = Flask(__name__)

# 환경 변수 세팅
app.config.from_object(Config)

# JWT 토큰 만들기
jwt = JWTManager(app)



api = Api(app)

# resources 와 연결
api.add_resource(UserRegisterResource, '/v1/user/register')   # 회원가입



# 기본 루트 연결 확인 멘트
@app.route('/')
def route_page():
    return "hello!!!!! it is work~"




if __name__ == "__main__" :
    app.run()


