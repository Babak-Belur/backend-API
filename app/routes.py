from app import app
from app.controller import UserController

@app.route('/')
def index():
    return 'Hello Flask App'


#users
@app.route('/users', methods=['GET'])
def users():
    return UserController.index()

@app.route('/users/<id>', methods=['GET'])
def detailUser(id):
    return UserController.detail(id)



#target
