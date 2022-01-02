from flask import request, abort
from flask_restful import Resource
from sqlalchemy.orm import joinedload
from flask_restful import Resource, fields, marshal
from flask_restful import reqparse, abort, Api, Resource
from flasgger import swag_from
from marshmallow import ValidationError

from app.models.order import Order, OrderItem
from app.shared.models import db
from app.shared.tasks import celery
from app.resources.schemas import OrderItemSchema, OrderSchema, OrderQuerySchema


class OrdersListViewSet(Resource):
    schema = OrderSchema()
    query_schema = OrderQuerySchema()

    @swag_from("docs/orders_list.yml")
    def get(self, *args, **kwargs):
        errors = self.query_schema.validate(request.args)
        if errors:
            abort(str(errors))

        orders_query = Order.query.options(joinedload(Order.order_items))
        if request.args:
            orders = orders_query.filter(
                Order.order_status == request.args["order_status"]
            )
        else:
            orders = orders_query.all()

        return self.schema.dump(orders, many=True)

    @swag_from("docs/order_create.yml")
    def post(self, *args, **kwargs):
        item_json = request.get_json()
        try:
            order = self.schema.load(item_json)
            order.save()
        except ValidationError as err:
            return err.messages, 400

        order_data = self.schema.dump(order)
        r = celery.send_task("tasks.process_order", kwargs={"data": order_data})
        order_data["promise"] = r.id
        return order_data, 200


class OrderDetailViewSet(Resource):
    schema = OrderSchema()

    @swag_from("docs/order_complete.yml")
    def post(self, promise, *args, **kwargs):
        result = celery.AsyncResult(promise).result
        if not result:
            return {"error": "Not found"}, 404

        order = Order.get(id=result["id"])
        order.order_status = result["order_status"]
        order.save()
        return self.schema.dump(order), 200
