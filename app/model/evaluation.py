from app import db 
from app.model.users import Users
from app.model.courseSubject import CourseSubject
from app.model.target import Target

class Evaluation(db.Model):
    id_evaluation = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_user = db.Column(db.BigInteger, db.ForeignKey(Users.id_user, ondelete='CASCADE', onupdate='CASCADE'))
    date = db.Column(db.Date, nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    study_time = db.Column(db.Enum('1', '2', '3', '4'), nullable=False)
    freetime = db.Column(db.Enum('1', '2', '3', '4', '5'), nullable=False)
    id_course = db.Column(db.BigInteger, db.ForeignKey(CourseSubject.id_course, ondelete='CASCADE', onupdate='CASCADE'))
    id_target = db.Column(db.BigInteger, db.ForeignKey(Target.id_target, ondelete='CASCADE', onupdate='CASCADE'))
    

    def __repr__(self):
        return '<Evaluation {}>'.format(self.name)