
from peewee import *
from datetime import date

db = SqliteDatabase("lab.db")


class Vehicle(Model):
    id_vehicle = PrimaryKeyField()
    mark = TextField()
    date = DateField()
    color = TextField()

    class Meta:
        database = db


class Sender(Model):
    id_sender = PrimaryKeyField()
    last_name = TextField()
    name = TextField()
    patronymic= TextField()
    birth = DateField()
    code = TextField()
    city = TextField()
    street = TextField()
    house = TextField()
    flat = TextField()
    phone= TextField()

    class Meta:
        database = db


class Order(Model):
    id_order = PrimaryKeyField()
    id_sender = IntegerField()
    id_recipient = IntegerField()
    date = DateField()
    delivery_date = DateField()
    delivery_price = FloatField()
    id_courier = IntegerField()
    id_vehicle= IntegerField()

    class Meta:
        database = db


db.create_tables([Vehicle, Sender, Order])

transport_1 = Vehicle(mark="BMW", date=date(2023, 6, 1), color="Black")
transport_1.save()

transport_2 = Vehicle(mark="Tesla", date=date(2021, 8, 15), color="Red")
transport_2.save()

sender_1 = Sender(last_name="Ivanov",name="Ivan", patronymic="Ivanovich",
                      birth=date(1980, 10, 10), code="101000", city="Saint Petersburg",
                      street="Nevsky Prospect", house="10", flat="45", phone="89030001234")
sender_1.save()

sender_2 = Sender(last_name="Petrov", name="Petr", patronymic="Petrovich",
                     birth=date(1990, 5, 25), code="200020", city="Moscow",
                      street="Tverskaya", house="25", flat="12", phone="89215556677")
sender_2.save()

order_1 = Order(id_sender=2, id_recipient=1, date=date(2024, 11, 10),
                delivery_date=date(2024, 11, 12), delivery_price=150.75, id_courier=2, id_vehicle=1)
order_1.save()

order_2 = Order(id_sender=1, id_recipient=2, date=date(2024, 11, 13),
                delivery_date=date(2024, 11, 14), delivery_price=200.40, id_courier=2, id_vehicle=2)
order_2.save()
