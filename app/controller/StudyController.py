from app.model.users import Users
from app.model.studyReport import StudyReport
from app.model.courseSubject import CourseSubject

from app import response, app, db
from flask import request

# Get all Study report
def index():
    try:
        study_report = StudyReport.query.all()
        data = formatarray(study_report)
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
        'id_study_report': data.id_study_report,
        'id_user': data.id_user,
        'date': data.date,
        'study_time': data.study_report,
        'id_course': data.id_course
    }

    return data


# get target by user id
def detailStudy(id):
    try:
        user = Users.query.filter_by(id_user=id).first()
        study_report = StudyReport.query.filter(StudyReport.id_user == id)

        if not user:
            return response.badRequest([], 'Tidak ada datanya')
        
        dataStudy = formatStudy(study_report)

        data = singleDetailStudy(user, dataStudy)

        return response.success(data, "success")

    except Exception as e:
        print(e)


def singleDetailStudy(user, study):
    data = {
        'id_user': user.id_user,
        'username': user.username,
        'name': user.name,
        'role': user.role,
        'study_report': study
    }

    return data


def singleStudy(study):
    data = {
        'id_study_report': study.id_study_report,
        'id_user': study.id_user,
        'date': study.date,
        'study_time': study.study_report,
        'id_course': study.id_course
    }

    return data

def formatStudy(data):
    array = []
    for i in data:
        array.append(singleStudy(i))
    return array
