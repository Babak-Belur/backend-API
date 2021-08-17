from app import db 
from app.model.users import Users

class Factor(db.Model):
    id_factor = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_user = db.Column(db.BigInteger, db.ForeignKey(Users.id_user))
    study_time = db.Column(db.Integer, nullable=False)
    g1 = db.Column(db.Integer, nullable=False)
    freetime = db.Column(db.Integer, nullable=False)
    health = db.Column(db.Enum('1', '2', '3', '4', '5'), nullable=False)
    extra_paid_course = db.Column(db.Enum('yes', 'no'), nullable=False)
    take_higher_education = db.Column(db.Enum('yes', 'no'), nullable=False)
    extracurricular = db.Column(db.Enum('yes', 'no'), nullable=False)

    def __repr__(self):
        return '<Factor {}>'.format(self.name)