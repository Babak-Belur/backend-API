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