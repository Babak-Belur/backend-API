from app.model.users import Users
from app.model.evaluation import Evaluation
from app.model.courseSubject import CourseSubject

from app import response, app, db
from flask import request

# Get all Study report
def index():
    try:
        evaluations = Evaluation.query.all()
        data = formatarray(evaluations)
        return response.success(data, "success")
    except Exception as e:
        print(e)


def formatarray(datas):
    array = []

    for i in datas:
        array.append(singleObject(i))

    return array


def singleObject(data):
    data = {
        'id_evaluation': data.id_evaluation,
        'id_user': data.id_user,
        'grade': data.grade,
        'id_course': data.id_course
    }

    return data


# get target by user id
def detailEvaluation(id):
    try:
        user = Users.query.filter_by(id_user=id).first()
        evaluation = Evaluation.query.filter(Evaluation.id_user == id)

        if not user:
            return response.badRequest([], 'Tidak ada datanya')
        
        dataEvaluation = formatEvaluation(evaluation)

        data = singleDetailEvaluation(user, dataEvaluation)

        return response.success(data, "success")

    except Exception as e:
        print(e)


def singleDetailEvaluation(user, evaluation):
    data = {
        'id_user': user.id_user,
        'username': user.username,
        'name': user.name,
        'role': user.role,
        'evaluation': evaluation
    }

    return data


def singleEvaluation(evaluation):
    data = {
        'id_evaluation': evaluation.id_evaluation,
        'id_user': evaluation.id_user,
        'grade': evaluation.grade,
        'id_course': evaluation.id_course
    }

    return data

def formatEvaluation(data):
    array = []
    for i in data:
        array.append(singleEvaluation(i))
    return array


# add evaluation
def save():
    try:
        id_user = request.form.get('id_user')
        grade = request.form.get('grade')
        id_course = request.form.get('id_course')

        evaluations = Evaluation(id_user=id_user, grade=grade, id_course=id_course)
        
        db.session.add(evaluations)
        db.session.commit()

        return response.success('', 'Success adding User Evaluation')
    except Exception as e:
        print(e)