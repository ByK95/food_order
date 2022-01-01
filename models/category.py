from app.shared.models import db

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    foods = db.relationship('Food', backref='category', lazy=True)