from app import app
from app.controller import UserController, DetailController

@app.route('/')
def index():
    return 'Hello Flask App'

@app.route('/users', methods=['GET'])
def users():
    return UserController.index()

@app.route('/users/<id>', methods=['GET'])
def detailUser(id):
    return UserController.detail(id)

@app.route('/detail/', methods=['GET'])
def detail():
    return DetailController.indexDetail()