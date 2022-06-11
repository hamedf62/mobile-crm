from email.policy import default
from enum import unique
from fnmatch import fnmatchcase
from sqlalchemy import DATETIME, Column, Boolean,LargeBinary, VARCHAR, ForeignKey, Text, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base, relation, backref
from datetime import datetime
from bcrypt import hashpw, gensalt

Base = declarative_base()

class UsersCategories(Base):
    __tablename__ = "users_categories"
    id = Column(Integer,primary_key=True)
    name = Column(VARCHAR)

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True)
    cat_id =Column(Integer, ForeignKey("users_categories.id"))
    mobile = Column(VARCHAR)
    _password = Column(LargeBinary)
    email = Column(Text)
    nid = Column(Integer)
    address = Column(Text)
    fname = Column(VARCHAR)
    lname = Column(VARCHAR)

    @property
    def password(self):
        raise AttributeError("password not readable")

    @password.setter
    def password(self, plaintext):
        if plaintext:
            self._password = hashpw(plaintext.encode("utf-8"), gensalt())
   
    category = relation(UsersCategories, backref=backref("users"))

class ProductsCategories(Base):
    __tablename__ = "products_categories"
    id = Column(Integer,primary_key=True)
    name = Column(VARCHAR)


class Products(Base):
    __tablename__ = "products"
    id = Column(Integer,primary_key=True)
    cat_id = Column(Integer, ForeignKey("products_categories.id"))
    name = Column(VARCHAR)
    price = Column(Float)

    category = relation(ProductsCategories,backref=backref("products"))

    invoices = relation("Invoices",secondary="invoice_product" )


class Invoices(Base):
    __tablename__ = "invoices"
    id = Column(Integer,primary_key=True)
    customer_id = Column(Integer,ForeignKey("users.id"))
    date = Column(DATETIME,default=datetime.now())
    
    customer = relation(Users,backref=backref("invoices") )
    products = relation("Products",secondary="invoice_product" )

class InvoiceProduct(Base):
    __tablename__ = "invoice_product"
    id = Column(Integer,primary_key=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    product_id = Column(Integer,ForeignKey("products.id"))
    quantity = Column(Integer, default=1)
