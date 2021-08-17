from app import db 
from app.model.users import Users
from app.model.course_subject import Course_Subject

class Study_Report(db.Model):
    id_evaluation = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_user = db.Column(db.BigInteger, db.ForeignKey(Users.id_user))
    date = db.Column(db.Date, default=datetime.now, nullable=False)
    study_time = db.Column(db.Integer(50), nullable=False)
    id_course = db.Column(db.BigInteger, db.ForeignKey(Course_Subject.id_course))
    
    def __repr__(self):
        return '<Study_Report {}>'.format(self.name)