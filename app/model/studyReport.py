from app import db 
from app.model.users import Users
from app.model.courseSubject import CourseSubject

class StudyReport(db.Model):
    id_evaluation = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_user = db.Column(db.BigInteger, db.ForeignKey(Users.id_user))
    date = db.Column(db.Date, nullable=False)
    study_time = db.Column(db.Integer, nullable=False)
    id_course = db.Column(db.BigInteger, db.ForeignKey(CourseSubject.id_course))
    
    def __repr__(self):
        return '<StudyReport {}>'.format(self.name)