from app.shared.models import db

class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    restourant_id = db.Column(db.Integer, db.ForeignKey('restourant.id'),nullable=False)
    