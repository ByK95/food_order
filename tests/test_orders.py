import json
from unittest import mock

from app.tests.test_base import BaseTestCase
from app.models.order import OrderItem, Order
from app.models.category import Category
from app.models.food import Food
from app.models.restourant import Restourant
from app.models.user import User


class OrderTestCase(BaseTestCase):
    def setUp(self):
        super().setUp()
        restourant = Restourant(name="Süper Dönerci")
        restourant.save()
        category1 = Category(name="Döner/Kebap")
        category1.save()
        self.food = Food(
            name="Döner", category_id=category1.id, restourant_id=restourant.id
        )
        self.food.save()
        self.order1 = Order(order_status="200")
        self.order1.save()
        self.order2 = Order(order_status="400")
        self.order2.save()
        self.order_item1 = OrderItem(order_id=self.order1.id, food_id=self.food.id)
        self.order_item1.save()
        self.order_item2 = OrderItem(order_id=self.order2.id, food_id=self.food.id)
        self.order_item2.save()

    def test_order_create_err_messages(self):
        response = self.client.post(
            "/orders/", json={"order_status": "300", "order_items": [{"food_id": 1}]}
        )
        self.assertEqual(response.status, "400 BAD REQUEST")
        self.assertEqual(response.json, {"order_status": ["Unknown field."]})

    def test_order_create_request(self):
        response = self.client.post("/orders/", json={"order_items": [{"food_id": 1}]})

        self.assertEqual(response.status, "200 OK")

        order = Order.get(id=3)

        self.assertEqual(order.order_status, "100")
        self.assertEqual(len(order.order_items), 1)
        self.assertEqual(order.order_items[0].food_id, 1)

    def test_get_order_list_response(self):
        response = self.client.get("/orders/")

        self.assertEqual(response.status, "200 OK")

        response_data = response.json

        self.assertEqual(len(response_data), 2)
        self.assertIn("order_items", response_data[0])

    @mock.patch("app.resources.orders.celery")
    def test_order_status_change_request(self, mock_celery):
        mock_celery.AsyncResult().result = {"id": 1, "order_status": 200}
        response = self.client.post("/orders/1/complete", json={})
        self.assertEqual(response.status, "200 OK")
