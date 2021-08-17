from app import app
from app.controller import UserController, TargetController, CourseController, FactorController

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
@app.route('/target', methods=['GET'])
def target():
    return TargetController.index()

@app.route('/target/<id>', methods=['GET'])
def targetUser(id):
    return TargetController.detailTarget(id)


#course
@app.route('/course', methods=['GET'])
def course():
    return CourseController.index()



#factor
@app.route('/factor', methods=['GET'])
def factor():
    return FactorController.index()