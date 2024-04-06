import pydantic
import typing


class ModifyBaseModel(pydantic.BaseModel):
    id: typing.Optional[int] = 0


class ChangePassword(pydantic.BaseModel):
    password: str


class LoginData(pydantic.BaseModel):
    login: str
    password: str


class Post(ModifyBaseModel):
    name: str


class User(ModifyBaseModel):
    position: int
    login: str
    password: str


class Cart(ModifyBaseModel):
    date_of_issue: str
    last_visite: str
    next_visite: str


class Polis(ModifyBaseModel):
    date_expired: str


class Documentation(ModifyBaseModel):
    number_and_seria: str
    cart: int
    polis: int


class Pathient(ModifyBaseModel):
    fio: str
    gender: str
    birthdate: str
    address: str
    phone: str
    email: str
    document: int


class Specialization(ModifyBaseModel):
    name: str


class Doctor(ModifyBaseModel):
    fio: str
    specialization: int


class Event(ModifyBaseModel):
    date_event: str
    doctor: int
    pathient: int

