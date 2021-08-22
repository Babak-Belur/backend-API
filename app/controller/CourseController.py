from app.model.courseSubject import CourseSubject

from app import response, app, db
from flask import request
from sqlalchemy import text

# Get all course
def index():
    try:
        courses = CourseSubject.query.all()
        data = formatarray(courses)
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
        'id_course': data.id_course,
        'course_name': data.course_name,
        'description': data.description,
    }

    return data

#try revoke code
#def index():
#    try:
#        data = {}
#        courses = CourseSubject.query.all()
#        response['id_course'] = courses.id_course
#        response['course_name'] = courses.course_name
#        response['description'] = courses.description
#        response['status_code'] = 200
#        datas = jsonify(data)
#        return response.success(datas, "success")
#
#    except Exception as e:
#        print(e)


# Get course by id
def detailCourse(id):
    try:
        course = CourseSubject.query.get(1)
        data = singleObjectCourse(course)
        return response.success(data, "success")
    except Exception as e:
        print(e)

#def detailCourse(id):
#    try:
#        data = {}
#        course = CourseSubject.query.get(id)
#        response['id_course'] = course.id_course
#        response['course_name'] = course.course_name
#        response['description'] = course.description
#        response['status_code'] = 200
#        return jsonify(data)

#    except Exception as e:
#        print(e)


def formatArray(datas):
    array = []

    for i in datas:
        array.append(singleObjectCourse(i))

    return array


def singleObjectCourse(data):
    data = {
        'id_course': data.id_course,
        'course_name': data.course_name,
        'description': data.description,
    }

    return data


#add course
def save():
    try:
        course_name = request.form.get('course_name')
        description = request.form.get('description')

        courses = CourseSubject(course_name=course_name, description=description)
        db.session.add(courses)
        db.session.commit()

        return response.success('', 'Success adding Course Subject')
    except Exception as e:
        print(e)


#edit course
def edit(id):
    try:
        course_name = request.form.get('course_name')
        description = request.form.get('description')

        data = [
            {
                'course_name': course_name,
                'description': description
            }
        ]

        course = CourseSubject.query.filter_by(id_course=id).first()

        course.course_name
        course.description

        db.session.commit()

        return response.success(data, 'Sukses update data')
    except Exception as e:
        print(e)

#hapus course
def hapus(id):
    try:
        course = CourseSubject.query.filter_by(id_course=id).first()
        if not course:
            return response.badRequest([], 'Data Course kosong')

        db.session.delete(course)
        db.session.commit()

        return response.success('', 'Berhasil Menghapus data')

    except Exception as e:
        print(e)