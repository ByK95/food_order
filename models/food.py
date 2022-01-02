from app.shared.models import db
from app.models.mixins import ModelMixin


class Food(ModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    restourant_id = db.Column(
        db.Integer, db.ForeignKey("restourant.id"), nullable=False
    )
