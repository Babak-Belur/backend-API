from app import db 
from app.model.users import Users

class DetailUser(db.Model):
    id_detail_user = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    age = db.Column(db.BigInteger, nullable=True)
    genre = db.Column(db.Enum('Male', 'Female'), nullable=True)
    internet = db.Column(db.Enum('Yes', 'No'), nullable=True)
    fjob = db.Column(db.String(50), nullable=True)
    mjob = db.Column(db.String(50), nullable=True)
    pstatus = db.Column(db.Enum('Yes', 'No'), nullable=True)
    id_user = db.Column(db.BigInteger, db.ForeignKey(Users.id_user, ondelete='CASCADE', onupdate='CASCADE'))

    def __repr__(self):
        return '<DetailUser {}>'.format(self.name)