from app.shared.models import db
from app.models.mixins import ModelMixin


class Restourant(ModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    foods = db.relationship("Food", backref="restourant", lazy=True)
