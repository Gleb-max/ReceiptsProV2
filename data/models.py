from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String, nullable=False, index=True, unique=True)
    email = db.Column(db.String, nullable=True)
    name = db.Column(db.String, nullable=True)
    tg_id = db.Column(db.Integer, nullable=True)

    # receipts = orm.relation("Receipt", back_populates="user")

    def __init__(self, phone, email, name):
        self.phone = phone
        self.email = email
        self.name = name

    def __str__(self):
        return f"<User phone = {self.phone}>"

    def __repr__(self):
        return self.__str__()


class Receipt(db.Model, UserMixin, SerializerMixin):
    __tablename__ = "receipts"

    id = db.Column(db.Integer,
                   primary_key=True, autoincrement=True)
    scan_code = db.Column(db.String,
                          index=True, unique=False, nullable=False)
    receipt = db.Column(db.Binary, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer,
                        db.ForeignKey("users.id"))

    # user = orm.relation("User")

    def __str__(self):
        return f"<Receipt scan_code = {self.scan_code}>"

    def __repr__(self):
        return self.__str__()
