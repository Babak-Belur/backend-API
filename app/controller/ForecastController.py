import json
from app.model.users import Users
from app.model.target import Target
from app.model.evaluation import Evaluation
from app.model.courseSubject import CourseSubject

from app import response, app, db
from flask import request
from flask import jsonify
from sqlalchemy import text
import tensorflow as tf
from keras.models import load_model


model = load_model('C:/Users/hp/Documents/backend-API/GF_V2_model.h5')

def prediction(id):
    evaluation = db.engine.execute(
            text("SELECT e.study_time, e.freetime, t.g1, e.grade FROM evaluation e inner join target t on t.id_target = e.id_target inner join users u on u.id_user = e.id_user inner join course_subject c on c.id_course = t.id_course where id_evaluation = :evaluation").params(evaluation=id)
    )


    data = formatArray(evaluation)

    studyTime = int(data[0]['study_time']) / 4
    freeTime = int(data[0]['freetime']) / 5
    G1 = int(data[0]['g1']) / 100
    G2 = int(data[0]['grade']) / 100
    
    input_data = [[studyTime, freeTime, G1, G2]]

    prediction = model.predict(input_data)

    lists = prediction.tolist()

    flatList = [ item for elem in prediction for item in elem]

    strings = [str(integer) for integer in flatList]
    a_string = "".join(strings)
    an_integer = float(a_string)

    datas = [
        {
            'study_time': data[0]['study_time'],
            'freetime': data[0]['freetime'],
            'g1': data[0]['g1'],
            'grade': data[0]['grade'],
            'predict_grade': an_integer
        }
    ]

    return response.success(datas, "sukses")


def formatArray(datas):
    array = []

    for i in datas:
        array.append(singleObjectEvaluation(i))

    return array


def singleObjectEvaluation(data):
    data = {
            'study_time': data.study_time,
            'freetime': data.freetime,
            'g1': data.g1,
            'grade': data.grade
    }

    return data