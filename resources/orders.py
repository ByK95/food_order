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

class OrdersViewSet(Resource):
    paginate_by = 20
    schema = OrderSchema()

    @swag_from('docs/orders.yml')
    def get(self, page=0, *args, **kwargs):
        orders = Order.query.options(joinedload(Order.order_items)).all()
        # .paginate(page=page, per_page=self.paginate_by)
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