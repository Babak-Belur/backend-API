from app import db 

class CourseSubject(db.Model):
    id_course = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    course_name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<CourseSubject {}>'.format(self.name)