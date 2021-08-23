from app.model.users import Users
from app.model.detailUser import DetailUser

from app import response, app, db
from flask import request


# Get all users
def index():
    try:
        users = Users.query.all()

        if not course:
            return response.badRequest([], 'Data User kosong, Id tidak ditemukan')

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
        detail_user = DetailUser.query.filter(DetailUser.id_user == id)

        if not user:
            return response.badRequest([], 'Tidak ada datanya, Id tidak ditemukan')

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


#add user
def save():
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        name = request.form.get('name')
        role = request.form.get('role')

        data = [
            {
                'username': username,
                'password': password,
                'name': name,
                'role': role
            }
        ]

        users = Users(username=username, password=password, name=name, role=role)
        #detail = Users.query.filter_by(username=username).first()
        detailUser = DetailUser(id_user=users.id_user)
        
        users.setPassword(password)
        db.session.add(users)
        db.session.add(detailUser)
        db.session.commit()

        return response.success(data, 'Success adding Users')
    except Exception as e:
        print(e)

#edit course
def edit(id):
    try:
        username = request.form.get('username')
        password = request.form.get('password')
        name = request.form.get('name')
        age = request.form.get('age')
        genre = request.form.get('genre')
        internet = request.form.get('internet')
        fjob = request.form.get('fjob')
        mjob = request.form.get('mjob')
        pstatus = request.form.get('pstatus')

        data = [
            {
                'username': username,
                'password': password,
                'name': name,
                'age': age,
                'genre': genre,
                'internet': internet,
                'fjob': fjob,
                'mjob': mjob,
                'pstatus': pstatus
            }
        ]

        user = Users.query.filter_by(id_user=id).first()
        datail = DetailUser.query.filter_by(id_detail_user=id).first()

        if not user:
            return response.badRequest([], 'Data user kosong, Id tidak ditemukan')

        user.username = username
        user.password = password
        user.name = name
        datail.age = age
        datail.genre = genre
        datail.internet = internet
        datail.fjob = fjob
        datail.mjob = mjob
        datail.pstatus = pstatus
        datail.id_user = id

        #db.session.add(course)
        db.session.commit()

        return response.success(data, 'Sukses update data')
    except Exception as e:
        print(e)


#delete user & detail user
def hapus(id):
    try:
        user = Users.query.filter_by(id_user=id).first()
        detail = DetailUser.query.filter_by(id_user=id).first()

        if not course:
            return response.badRequest([], 'Data User kosong, Id tidak ditemukan')

        db.session.delete(user)
        db.session.delete(detail)
        db.session.commit()

        return response.success('', 'Berhasil Menghapus data')

    except Exception as e:
        print(e)