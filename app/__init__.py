from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.model import users, detail_user, course_subject, evaluation, factor, study_report, target
from app import routes