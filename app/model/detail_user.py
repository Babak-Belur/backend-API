from app import db 
from app.model.users import Users

class Detail_User(db.Model):
    id_detail_user = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    age = db.Column(db.BigInteger, nullable=False)
    genre = db.Column(db.Enum('Male', 'Female'), nullable=False)
    internet = db.Column(db.Enum('Yes', 'No'), nullable=False)
    fjob = db.Column(db.String(50), nullable=False)
    mjob = db.Column(db.String(50), nullable=False)
    pstatus = db.Column(db.Enum('Yes', 'No'), nullable=False)
    id_user = db.Column(db.BigInteger, db.ForeignKey(Users.id_user))

    def __repr__(self):
        return '<Detail_User {}>'.format(self.name)