from app.shared.models import db
from app.shared.enums import OrderStatusEnum


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_items = db.relationship('OrderItem', backref='order', lazy=True)
    order_status = db.Column(db.String(4), nullable=False)

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'),nullable=False)
    food_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    # food = db.relationship("Food")
    # category = db.relationship("Category")

    def save(self):
        db.session.add(self)
        db.session.commit()