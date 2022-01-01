from marshmallow import Schema, fields, post_load

from app.models.order import Order, OrderItem


class OrderItemSchema(Schema):
    id = fields.Integer()
    order_id = fields.Integer()
    food_id = fields.Integer()

class OrderSchema(Schema):
    id = fields.Integer()
    order_items = fields.Nested(OrderItemSchema, many=True)
    order_status = fields.String()

    @post_load
    def make_user(self, data, **kwargs):
        return Order(**data)