from extensions import db

class Tip(db.Model):
    __tablename__ = 'tips'

    id = db.Column(db.Integer, primary_key=True)
    published_date = db.Column(db.String(20), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    detail = db.Column(db.Text, nullable=False)
    source = db.Column(db.String(300), nullable=False)
    
