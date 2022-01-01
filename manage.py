import os
from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from flasgger import Swagger

from app.resources.orders import OrdersListViewSet, OrderDetailViewSet
from app.shared.models import db 
from app.models.order import Order, OrderItem
from app.models.category import Category
from app.models.food import Food
from app.models.restourant import Restourant
from app.models.user import User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)
swagger = Swagger(app)


api.add_resource(OrdersListViewSet, '/orders/')
api.add_resource(OrderDetailViewSet, 
    '/orders/<int:order_id>/ready',
)


if __name__ == "__main__":
    app.run(debug=True)