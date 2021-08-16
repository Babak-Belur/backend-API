from app import app
from app.controller import UserController

@app.route('/')
def index():
    return 'Hello Flask App'

@app.route('/users', methods=['GET'])
def users():
    return UserController.index()