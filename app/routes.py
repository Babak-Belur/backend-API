from app import app
from flask import request
from app.controller import UserController, TargetController, CourseController, EvaluationController

@app.route('/')
def index():
    return 'Hello Flask App'


#users
@app.route('/users', methods=['GET','POST'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.save()

@app.route('/users/<id>', methods=['GET'])
def detailUser(id):
    return UserController.detail(id)



#target
@app.route('/target', methods=['GET','POST'])
def target():
    if request.method == 'GET':
        return TargetController.index()
    else:
        return TargetController.save()
    

@app.route('/target/<id>', methods=['GET'])
def targetUser(id):
    return TargetController.detailTarget(id)


#course
@app.route('/course', methods=['GET','POST'])
def course():
    if request.method == 'GET':
        return CourseController.index()
    else:
        return CourseController.save()

@app.route('/course/<id>', methods=['GET', 'PUT', 'DELETE'])
def course_subject(id):
    if request.method == 'GET':
        return CourseController.detailCourse(id)
    elif request.method == 'PUT':
        return CourseController.edit(id)
    elif request.method == 'DELETE':
        return CourseController.hapus(id)


#evaluation
@app.route('/evaluation', methods=['GET','POST'])
def evaluation():
    if request.method == 'GET':
        return EvaluationController.index()
    else:
        return EvaluationController.save()


@app.route('/evaluation/<id>', methods=['GET'])
def evaluationUser(id):
    return EvaluationController.detailEvaluation(id)