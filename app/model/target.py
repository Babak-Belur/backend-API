from app import db 
from app.model.users import Users
from app.model.courseSubject import CourseSubject

class Target(db.Model):
    id_target = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_user = db.Column(db.BigInteger, db.ForeignKey(Users.id_user))
    id_course = db.Column(db.BigInteger, db.ForeignKey(CourseSubject.id_course))
    g1 = db.Column(db.Integer, nullable=False)
    grade_target = db.Column(db.Integer, nullable=False)
    target_time = db.Column(db.Date, nullable=False)
    achived = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return '<Target {}>'.format(self.name)