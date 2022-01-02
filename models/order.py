from app.shared.models import db
from app.shared.enums import OrderStatusEnum
from app.models.mixins import ModelMixin


class Order(ModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_items = db.relationship("OrderItem", backref="order", lazy=True)
    order_status = db.Column(db.String(4), default="100", nullable=False)


class OrderItem(ModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey("food.id"), nullable=False)
    # food = db.relationship("Food")
    # category = db.relationship("Category")
