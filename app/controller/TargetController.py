from app.model.users import Users
from app.model.target import Target
from app.model.courseSubject import CourseSubject

from app import response, app, db
from flask import request
from sqlalchemy import text

# Get all target
def index():
    try:
        target = db.engine.execute(
            text("SELECT * FROM target t inner join course_subject c on t.id_course = c.id_course inner join users u on u.id_user = t.id_user")
        )

        if not target:
            return response.badRequest([], 'Data Target kosong, Id tidak ditemukan')

        data = formatarray(target)

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
        'id_target': data.id_target,
        'g1': data.g1,
        'grade_target': data.grade_target,
        'target_time': data.target_time,
        'achived': data.achived,
        'course':[
            {
                'id_course': data.id_course,
                'course_name': data.course_name,
                'description': data.description
            }
        ],
        'user':[
            {
                'id_user': data.id_user,
                'name': data.name,
                'username': data.username
            }
        ]
    }

    return data


# get target by user id
def detailUserTarget(id):
    try:
        users = Users.query.filter_by(id_user=id).first()
        target_id = id
        target = db.engine.execute(
            text("SELECT * FROM target t inner join course_subject c on t.id_course = c.id_course where id_user = :user").params(user=id)
        )

        if not target:
            return response.badRequest([], 'Tidak ada datanya')
        
        dataTarget = formatTarget(target)

        data = singleDetailTarget(users, dataTarget)

        return response.success(data, "success")

    except Exception as e:
        print(e)


def singleDetailTarget(users, target):
    data = {
        'id_user': users.id_user,
        'username': users.username,
        'name': users.name,
        'role': users.role,
        'target': target
    }

    return data


def singleTarget(target):
    data = {
        'id_target': target.id_target,
        'id_course': target.id_course,
        'g1': target.g1,
        'grade_target': target.grade_target,
        'target_time': target.target_time,
        'achived': target.achived,
        'course': [
            {
                'id_course': target.id_course,
                'course_name': target.course_name,
                'description': target.description
            }
        ]
    }

    return data

def formatTarget(data):
    array = []
    for i in data:
        array.append(singleTarget(i))
    return array


#get target id
def detailTarget(id):
    try:
        target = db.engine.execute(
            text("SELECT * FROM target t inner join course_subject c on t.id_course = c.id_course inner join users u on u.id_user = t.id_user where id_target = :target").params(target=id)
        )

        if not target:
            return response.badRequest([], 'Data Target kosong, Id tidak ditemukan')

        data = formatArray(target)

        return response.success(data, "success")
    except Exception as e:
        print(e)


def formatArray(datas):
    array = []

    for i in datas:
        array.append(singleObjectTarget(i))

    return array


def singleObjectTarget(data):
    data = {
        'id_target': data.id_target,
        'g1': data.g1,
        'grade_target': data.grade_target,
        'target_time': data.target_time,
        'achived': data.achived,
        'course':[
            {
                'id_course': data.id_course,
                'course_name': data.course_name,
                'description': data.description
            }
        ],
        'user':[
            {
                'id_user': data.id_user,
                'name': data.name,
                'username': data.username
            }
        ]
    }

    return data

#add target user
def save():
    try:
        id_user = request.form.get('id_user')
        id_course = request.form.get('id_course')
        g1 = request.form.get('g1')
        grade_target = request.form.get('grade_target')
        target_time = request.form.get('target_time')
        achived = request.form.get('achived')

        data = [
            {
                'id_user': id_user,
                'id_course': id_course,
                'g1': g1,
                'grade_target': grade_target,
                'target_time': target_time,
                'achived': achived,
            }
        ]

        targets = Target(id_user=id_user, id_course=id_course, g1=g1, grade_target=grade_target, target_time=target_time, achived=achived)
        
        db.session.add(targets)
        db.session.commit()

        return response.success(data, 'Success adding Target Users')
    except Exception as e:
        print(e)


# edit target
def edit(id):
    try:
        id_user = request.form.get('id_user')
        id_course = request.form.get('id_course')
        g1 = request.form.get('g1')
        grade_target = request.form.get('grade_target')
        target_time = request.form.get('target_time')
        achived = request.form.get('achived')

        data = [
            {
                'id_user': id_user,
                'id_course': id_course,
                'g1': g1,
                'grade_target': grade_target,
                'target_time': target_time,
                'achived': achived,
            }
        ]

        target = Target.query.filter_by(id_target=id).first()

        if not target:
            return response.badRequest([], 'Data Target kosong, Id tidak ditemukan')

        target.id_user = id_user
        target.id_course = id_course
        target.g1 = g1
        target.grade_target = grade_target
        target.target_time = target_time
        target.achived = achived

        #db.session.add(course)
        db.session.commit()

        return response.success(data, 'Sukses update data')
    except Exception as e:
        print(e)

#delete target
def hapus(id):
    try:
        target = Target.query.filter_by(id_target=id).first()

        if not target:
            return response.badRequest([], 'Data Target kosong, Id tidak ditemukan')

        db.session.delete(target)
        db.session.commit()

        return response.success('', 'Berhasil Menghapus data')

    except Exception as e:
        print(e)