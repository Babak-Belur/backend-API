from app import app, response
from flask import request
from app.controller import UserController, TargetController, CourseController, EvaluationController, ForecastController
from flask import request
from flask import jsonify
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required

@app.route('/')
def index():
    return 'Hello Flask App'


# testing jwt token
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return response.success(current_user, 'sukses')


#users
@app.route('/users', methods=['GET','POST'])
#@jwt_required()
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.save()

@app.route('/users/<id>', methods=['GET','PUT','DELETE'])
#@jwt_required()
def detailUser(id):
    if request.method == 'GET':
        return UserController.detail(id)
    elif request.method == 'PUT':
        return UserController.edit(id)
    elif request.method == 'DELETE':
        return UserController.hapus(id)


#login
@app.route('/login', methods=['POST'])
def login():
    return UserController.login()


#target
@app.route('/target', methods=['GET','POST'])
#@jwt_required()
def target():
    if request.method == 'GET':
        return TargetController.index()
    else:
        return TargetController.save()
    

@app.route('/target/<id>', methods=['GET','PUT','DELETE'])
#@jwt_required()
def targetDetail(id):
    if request.method == 'GET':
        return TargetController.detailTarget(id)
    elif request.method == 'PUT':
        return TargetController.edit(id)
    elif request.method == 'DELETE':
        return TargetController.hapus(id)

@app.route('/target/user/<id>', methods=['GET'])
#@jwt_required()
def targetUser(id):
    return TargetController.detailUserTarget(id)


#course
@app.route('/course', methods=['GET','POST'])
#@jwt_required()
def course():
    if request.method == 'GET':
        return CourseController.index()
    else:
        return CourseController.save()

@app.route('/course/<id>', methods=['GET', 'PUT', 'DELETE'])
#@jwt_required()
def course_subject(id):
    if request.method == 'GET':
        return CourseController.detailCourse(id)
    elif request.method == 'PUT':
        return CourseController.edit(id)
    elif request.method == 'DELETE':
        return CourseController.hapus(id)


#evaluation
@app.route('/evaluation', methods=['GET','POST'])
#@jwt_required()
def evaluation():
    if request.method == 'GET':
        return EvaluationController.index()
    else:
        return EvaluationController.save()


@app.route('/evaluation/<id>', methods=['GET','PUT','DELETE'])
#@jwt_required()
def evaluationDetail(id):
    if request.method == 'GET':
        return EvaluationController.detailEvaluation(id)
    elif request.method == 'PUT':
        return EvaluationController.edit(id)
    elif request.method == 'DELETE':
        return EvaluationController.hapus(id)
    

@app.route('/evaluation/user/<id>', methods=['GET'])
#@jwt_required()
def evaluationUser(id):
    return EvaluationController.detailUserEvaluation(id)


# get the prediction from model
@app.route('/predict/<id>', methods=['GET'])
#@jwt_required()
def predict(id):
    return ForecastController.prediction(id)