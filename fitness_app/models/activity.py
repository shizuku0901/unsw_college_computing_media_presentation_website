from extensions import db

class Activity(db.Model):
    __tablename__ = 'activities'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=False)
    activity_name = db.Column(db.String(200), nullable=False)
    time = db.Column(db.Integer, nullable=False)