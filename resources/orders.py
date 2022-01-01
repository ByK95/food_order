from flask import request
from flask_restful import Resource
from sqlalchemy.orm import joinedload
from flask_restful import Resource, fields, marshal
from flask_restful import reqparse, abort, Api, Resource
from flasgger import swag_from
from marshmallow import ValidationError

from app.models.order import Order, OrderItem
from app.shared.models import db
from app.resources.schemas import OrderItemSchema, OrderSchema

class OrdersListViewSet(Resource):
    schema = OrderSchema()

    @swag_from('docs/orders.yml')
    def get(self, *args, **kwargs):
        orders = Order.query.options(joinedload(Order.order_items)).all()
        return self.schema.dump(orders, many=True)

    @swag_from('docs/orders.yml')
    def post(self, *args, **kwargs):
        item_json = request.get_json()
        try:
            order = self.schema.load(item_json)
            order.save()
        except ValidationError as err:
            return err.messages, 400
    
        return self.schema.dump(order), 200

class OrderDetailViewSet(Resource):
    schema = OrderSchema()
    order_status_mapping = {
        "preparing" : '200',
        "ready": '300',
        "delivered": "400"
    }

    @swag_from('docs/orders.yml')
    def post(self, order_id, *args, **kwargs):
        order_status = self.order_status_mapping.get(request.url.rsplit('/')[-1])
        if not order_status:
            return {"status": "Invalid"} ,400
        order = Order.get(id=order_id)
        order.order_status = order_status
        order.save()
        return {}, 200
