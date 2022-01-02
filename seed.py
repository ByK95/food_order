# -*- coding: utf-8 -*-
import sys 
sys.path.append('/')

from app.shared.models import db
from app.models.order import Order, OrderItem
from app.models.category import Category
from app.models.food import Food
from app.models.restourant import Restourant
from app.models.user import User
from app.manage import app

def seed():
    a = User(name="user", surname="test", email="a@a.com")
    a.save()

    doner = Restourant(name="Süper Dönerci")
    ev = Restourant(name="Harika Ev Yemekleri")
    bufe = Restourant(name="Bizim Büfe ")

    db.session.add_all([doner, ev, bufe])
    db.session.commit()

    category1 = Category(name="Döner/Kebap")
    category2 = Category(name="Ev Yemekleri")
    category3 = Category(name="Fast-Food")

    db.session.add_all([category1, category2, category3])
    db.session.commit()

    foods = [
        Food(name="Döner", category_id=category1.id, restourant_id=doner.id),
        Food(name="İskender", category_id=category1.id, restourant_id=doner.id),
        Food(name="Etibol İskender ", category_id=category1.id, restourant_id=doner.id),
        Food(name="Kuru Fasülye", category_id=category2.id, restourant_id=ev.id),
        Food(name="Pilav", category_id=category2.id, restourant_id=ev.id),
        Food(name="Mercibek Çorbası", category_id=category2.id, restourant_id=ev.id),
        Food(name="Goralı", category_id=category3.id, restourant_id=bufe.id),
        Food(name="Dilli Kaşarlı", category_id=category3.id, restourant_id=bufe.id),
        Food(name="Yengen", category_id=category3.id, restourant_id=bufe.id),
    ]
    db.session.add_all(foods)
    db.session.commit()

    order = Order(order_status="200")
    db.session.add(order)
    db.session.commit()
    order_item = OrderItem(order_id=order.id, food_id=foods[0].id)
    db.session.add(order_item)
    db.session.commit()

def truncate_all():
    models = [OrderItem, Order, Food, Restourant, Category, User]
    for model in models:
        db.session.query(model).delete()
        db.session.commit()

if __name__ == "__main__":
    with app.app_context():
        truncate_all()
        seed()