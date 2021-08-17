from app.model.factor import Factor

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