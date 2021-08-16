from app.model.users import Users

from app import response, app, db
from flask import request

def index():
    try:
        users = Users.query.all()
        data = formatarray(users)
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
        'id_user': data.id_user,
        'username': data.username,
        'password': data.password,
        'name': data.name,
        'role': data.role
    }

    return data