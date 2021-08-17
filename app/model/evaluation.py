from app import db 
from app.model.users import Users
from app.model.course_subject import Course_Subject

class Evaluation(db.Model):
    id_evaluation = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_user = db.Column(db.BigInteger, db.ForeignKey(Users.id_user))
    grade = db.Column(db.Integer(50), nullable=False)
    id_course = db.Column(db.BigInteger, db.ForeignKey(Course_Subject.id_course))
    

    def __repr__(self):
        return '<Evaluation {}>'.format(self.name)