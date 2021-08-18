from app.model.courseSubject import CourseSubject

from app import response, app, db
from flask import request

# Get all users
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