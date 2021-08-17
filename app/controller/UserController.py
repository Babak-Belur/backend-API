from app.model.users import Users
from app.model.detail_user import Detail_User

from app import response, app, db
from flask import request


# Get all users
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


#get user & detail user by id
def detail(id):
    try:
        user = Users.query.filter_by(id_user=id).first()
        detail_user = Detail_User.query.filter(Detail_User.id_user == id)

        if not user:
            return response.badRequest([], 'Tidak ada datanya')

        dataDetail = formatDetail(detail_user)

        data = singleDetailUser(user, dataDetail)

        return response.success(data, "success")

    except Exception as e:
        print(e)


def singleDetailUser(user, detail):
    data = {
        'id_user': user.id_user,
        'username': user.username,
        'name': user.name,
        'role': user.role,
        'detail_user': detail
    }

    return data


def singleDetail(detail_user):
    data = {
        'id_detail_user': detail_user.id_detail_user,
        'age': detail_user.age,
        'gender': detail_user.genre,
        'internet': detail_user.internet,
        'fjob': detail_user.fjob,
        'mjob': detail_user.mjob,
        'pstatus': detail_user.pstatus
    }

    return data

def formatDetail(data):
    array = []
    for i in data:
        array.append(singleDetail(i))
    return array
