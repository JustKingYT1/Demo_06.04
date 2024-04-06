from peewee import *
import settings


db = SqliteDatabase(f'{settings.DB_DIR}/{settings.DB_NAME}')


class BaseModel(Model):
    class Meta:
        database = db


class Post(BaseModel):
    post = CharField(default='')
    power_level = IntegerField(default=0)


class User(BaseModel):
    position = ForeignKeyField(model=Post, default=0)
    login = CharField(default='')
    password = CharField(default='')


class Cart(BaseModel):
    date_of_issue = CharField(default='')
    last_visite = CharField(default='')
    next_visite = CharField(default='')


class Polis(BaseModel):
    date_expired = CharField(default='')


class Documentation(BaseModel):
    number_and_seria = CharField(default='')
    cart = ForeignKeyField(model=Cart, default=0)
    polis = ForeignKeyField(model=Polis, default=0)


class Pathient(BaseModel):
    fio = CharField(default='')
    gender = CharField(default='')
    birthdate = CharField(default='')
    address = CharField(default='')
    phone = CharField(default='')
    email = CharField(default='')
    document = ForeignKeyField(model=Documentation, default=0)


class Specialization(BaseModel):
    name = CharField(default='')


class Doctor(BaseModel):
    fio = CharField(default='')
    specialization = ForeignKeyField(model=Specialization, default=0)


class Event(BaseModel):
    date_event = CharField(default='')
    doctor = ForeignKeyField(model=Doctor, default=0)
    pathient = ForeignKeyField(model=Pathient, default=0)


db.create_tables([User, Post, Cart, Polis, Documentation, Pathient, Specialization, Doctor, Event])

