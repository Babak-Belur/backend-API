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
    #evaluation = db.engine.execute(
    #        text("SELECT e.study_time, e.freetime, t.g1, e.grade FROM evaluation e inner join target t on t.id_target = e.id_target inner join users u on u.id_user = e.id_user inner join course_subject c on c.id_course = t.id_course where id_evaluation = :evaluation").params(evaluation=id)
    #)

    #studyTime = evaluation.study_time / 4
    #freeTime = evaluation.freetime / 5
    studyTime = 3 / 4
    freeTime = 3 / 5

    G1 = 90 / 100
    G2 = 90 / 100
    #G1 = evaluation.g1 / 100
    #G2 = evaluation.grade / 100

    input_data = [[studyTime, freeTime, G1, G2]]

    prediction = model.predict(input_data)

    data = jsonify(prediction)

    return response.success(data, "sukses")
        