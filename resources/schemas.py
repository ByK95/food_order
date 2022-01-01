from marshmallow import Schema, fields, post_load

from app.models.order import Order, OrderItem


class OrderItemSchema(Schema):
    id = fields.Integer()
    order_id = fields.Integer()
    food_id = fields.Integer()

    @post_load
    def make_order_item(self, data, **kwargs):
        return OrderItem(**data)

class OrderSchema(Schema):
    id = fields.Integer()
    order_items = fields.Nested(OrderItemSchema, many=True)
    order_status = fields.String(dump_only=True)

    @post_load
    def make_order(self, data, **kwargs):
        return Order(**data)