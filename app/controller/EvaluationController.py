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


# edit evaluation
def edit(id):
    try:
        id_user = request.form.get('id_user')
        date = request.form.get('date')
        grade = request.form.get('grade')
        study_time = request.form.get('study_time')
        freetime = request.form.get('freetime')
        id_target = request.form.get('id_target')

        data = [
            {
                'id_user': id_user,
                'date': date,
                'grade': grade,
                'study_time': study_time,
                'freetime': freetime,
                'id_target': id_target,
            }
        ]

        evaluation = Evaluation.query.filter_by(id_evaluation=id).first()

        if not Evaluation:
            return response.badRequest([], 'Data Evaluation kosong, Id tidak ditemukan')

        evaluation.id_user = id_user
        evaluation.date = date
        evaluation.grade = grade
        evaluation.study_time = study_time
        evaluation.freetime = freetime
        evaluation.id_target = id_target

        #db.session.add(course)
        db.session.commit()

        return response.success(data, 'Sukses update data')
    except Exception as e:
        print(e)

#delete target
def hapus(id):
    try:
        evaluation = Evaluation.query.filter_by(id_evaluation=id).first()

        if not evaluation:
            return response.badRequest([], 'Data Evaluation kosong, Id tidak ditemukan')

        db.session.delete(evaluation)
        db.session.commit()

        return response.success('', 'Berhasil Menghapus data')

    except Exception as e:
        print(e)