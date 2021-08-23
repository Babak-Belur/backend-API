from app.model.users import Users
from app.model.evaluation import Evaluation
from app.model.courseSubject import CourseSubject

from app import response, app, db
from flask import request
from sqlalchemy import text

# Get all Study report
def index():
    try:
        evaluations = db.engine.execute(
            text("SELECT * FROM evaluation e inner join users u on e.id_user = u.id_user inner join target t on t.id_target = e.id_target inner join course_subject c on c.id_course = t.id_course")
        )

        if not evaluations:
            return response.badRequest([], 'Data Evaluation kosong, Id tidak ditemukan')

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
        'date': data.date,
        'grade': data.grade,
        'study_time': data.study_time,
        'freetime': data.freetime,
        'users': [
            {
                'id_user': data.id_user,
                'name': data.name,
                'username': data.username,
                'role': data.role
            }
        ],
        'targets': [
            {
                'id_target': data.id_target,
                'g1': data.g1,
                'grade_target': data.grade_target,
                'target_time': data.target_time,
                'achived': data.achived,
                'course': [
                    {
                        'id_course': data.id_course,
                        'course_name': data.course_name,
                        'description': data.description
                    }
                ]
            }
        ]
    }

    return data


# get target by user id
def detailUserEvaluation(id):
    try:
        user = Users.query.filter_by(id_user=id).first()
        evaluation_id = id
        evaluation = db.engine.execute(
            text("SELECT * FROM evaluation e inner join target t on t.id_target = e.id_target inner join course_subject c on c.id_course = t.id_course where e.id_user = :user").params(user=id)
        )

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
        'date': evaluation.date,
        'grade': evaluation.grade,
        'study_time': evaluation.study_time,
        'freetime': evaluation.freetime,
        'target': [
            {
                'id_target': evaluation.id_target,
                'g1': evaluation.g1,
                'grade_target': evaluation.grade_target,
                'target_time': evaluation.target_time,
                'achived': evaluation.achived,
                'course': [
                    {
                        'id_course': evaluation.id_course,
                        'course_name': evaluation.course_name,
                        'description': evaluation.description
                    }
                ]
            }
        ]
    }

    return data

def formatEvaluation(data):
    array = []
    for i in data:
        array.append(singleEvaluation(i))
    return array


#get evaluation id
def detailEvaluation(id):
    try:
        evaluation = db.engine.execute(
            text("SELECT * FROM evaluation e inner join target t on t.id_target = e.id_target inner join users u on u.id_user = e.id_user inner join course_subject c on c.id_course = t.id_course where id_evaluation = :evaluation").params(evaluation=id)
        )
        data = formatArray(evaluation)

        if not evaluation:
            return response.badRequest([], 'Data Target kosong, Id tidak ditemukan')

        return response.success(data, "success")
    except Exception as e:
        print(e)



def formatArray(datas):
    array = []

    for i in datas:
        array.append(singleObjectEvaluation(i))

    return array


def singleObjectEvaluation(data):
    data = {
        'id_evaluation': data.id_evaluation,
        'date': data.date,
        'grade': data.grade,
        'study_time': data.study_time,
        'freetime': data.freetime,
        'users': [
            {
                'id_user': data.id_user,
                'name': data.name,
                'username': data.username,
                'role': data.role
            }
        ],
        'targets': [
            {
                'id_target': data.id_target,
                'g1': data.g1,
                'grade_target': data.grade_target,
                'target_time': data.target_time,
                'achived': data.achived,
                'course': [
                    {
                        'id_course': data.id_course,
                        'course_name': data.course_name,
                        'description': data.description
                    }
                ]
            }
        ]
    }

    return data

# add evaluation
def save():
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

        evaluations = Evaluation(id_user=id_user, date=date, grade=grade, study_time=study_time, freetime=freetime, id_target=id_target)
        
        db.session.add(evaluations)
        db.session.commit()

        return response.success(data, 'Success adding User Evaluation')
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