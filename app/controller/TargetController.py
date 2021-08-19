from app.model.users import Users
from app.model.target import Target
from app.model.courseSubject import CourseSubject

from app import response, app, db
from flask import request

# Get all target
def index():
    try:
        target = Target.query.all()
        course_subject = CourseSubject.query.filter(CourseSubject.id_course == Target.id_course)
        
        #courseData = courseFormat(course)

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
        'id_user': data.id_user,
        'id_course': data.id_course,
        'grade': data.grade,
        'target_time': data.target_time,
        'achived': data.achived
    }

    return data

#def singleCourse(course):
#    data = {
#        'id_course': course.id_course,
#        'course_name': course.course_name,
#        'description': course.description,
#    }

#    return data

#def formatCourse(data):
#    array = []
#    for i in data:
#        array.append(singleCourse(i))
#    return array



# get target by user id
def detailTarget(id):
    try:
        user = Users.query.filter_by(id_user=id).first()
        target = Target.query.filter(Target.id_user == id)
        #course_subject = CourseSubject.query.filter(CourseSubject.id_course == Target.id_course)

        if not target:
            return response.badRequest([], 'Tidak ada datanya')

        #dataCourse = formatCourse(course_subject)

        #dataSingleTarget = singleDetailCourse(dataCourse, target)
        
        dataTarget = formatTarget(target)

        data = singleDetailTarget(user, dataTarget)

        return response.success(data, "success")

    except Exception as e:
        print(e)


def singleDetailTarget(user, target):
    data = {
        'id_user': user.id_user,
        'username': user.username,
        'name': user.name,
        'role': user.role,
        'target': target
    }

    return data


def singleTarget(target):
    data = {
        'id_target': target.id_target,
        'id_course': target.id_course,
        'grade': target.grade,
        'target_time': target.target_time,
        'achived': target.achived
    }

    return data

def formatTarget(data):
    array = []
    for i in data:
        array.append(singleTarget(i))
    return array

##########################################################
#def singleDetailCourse(target, course):
#    data = {
#        'id_target': target.id_target,
#        'grade': target.grade,
#        'target_time': target.target_time,
#        'achived': target.achived,
#        'course': course
#    }

#    return data


#def singleCourse(course):
#    data = {
#        'id_course': course.id_course,
#        'course_name': course.course_name,
#        'description': course.description,
#    }

#    return data

#def formatCourse(data):
#    array = []
#    for i in data:
#        array.append(singleCourse(i))
#    return array


#add target user
def save():
    try:
        id_user = request.form.get('id_user')
        id_course = request.form.get('id_course')
        grade = request.form.get('grade')
        target_time = request.form.get('target_time')
        achived = request.form.get('achived')

        targets = Target(id_user=id_user, id_course=id_course, grade=grade, target_time=target_time, achived=achived)
        
        db.session.add(targets)
        db.session.commit()

        return response.success('', 'Success adding Target Users')
    except Exception as e:
        print(e)