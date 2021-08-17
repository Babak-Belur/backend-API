from app.model.factor import Factor
from app.model.users import Users

from app import response, app, db
from flask import request

# Get all users
def index():
    try:
        factors = Factor.query.all()
        data = formatarray(factors)
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
        'id_factor': data.id_factor,
        'id_user': data.id_user,
        'study_time': data.study_time,
        'g1': data.g1,
        'freetime': data.freetime,
        'health': data.health,
        'extra_paid_course': data.extra_paid_course,
        'take_higher_education': data.take_higher_education,
        'extracurricular': data.extracurricular,
    }

    return data

#get factor & detail user by id
def detailFactor(id):
    try:
        user = Users.query.filter_by(id_user=id).first()
        factor = Factor.query.filter(Factor.id_user == id)

        if not user:
            return response.badRequest([], 'Tidak ada datanya')

        dataFactor = formatFactor(factor)

        data = singleDetailFactor(user, dataFactor)

        return response.success(data, "success")

    except Exception as e:
        print(e)


def singleDetailFactor(user, factor):
    data = {
        'id_user': user.id_user,
        'username': user.username,
        'name': user.name,
        'role': user.role,
        'factor': factor
    }

    return data


def singleFactor(factor):
    data = {
        'id_factor': factor.id_factor,
        'id_user': factor.id_user,
        'study_time': factor.study_time,
        'g1': factor.g1,
        'freetime': factor.freetime,
        'health': factor.health,
        'extra_paid_course': factor.extra_paid_course,
        'take_higher_education': factor.take_higher_education,
        'extracurricular': factor.extracurricular,
    }

    return data

def formatFactor(data):
    array = []
    for i in data:
        array.append(singleFactor(i))
    return array