from email.policy import default
from enum import unique
from fnmatch import fnmatchcase
from sqlalchemy import DATETIME, Column, Boolean, VARCHAR, ForeignKey, Text, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base, relation, backref
from datetime import datetime


Base = declarative_base()


class Customers(Base):
    __tablename__ = "customers"
    id = Column(Integer,primary_key=True)
    fname = Column(VARCHAR)
    lname = Column(VARCHAR)
    mobile = Column(VARCHAR)
    email = Column(Text)
    password = Column(VARCHAR)
    ncode = Column(Integer)
    address = Column(Text)

class Categories(Base):
    __tablename__ = "categories"
    id = Column(Integer,primary_key=True)
    name = Column(VARCHAR)

    # products = relation.....

class Products(Base):
    __tablename__ = "products"
    id = Column(Integer,primary_key=True)
    cat_id = Column(Integer, ForeignKey("categories.id"))
    name = Column(VARCHAR)
    price = Column(Float)

    category = relation(Categories,backref=backref("products"))

    invoices = relation("Invoices",secondary="invoice_product" )


class Invoices(Base):
    __tablename__ = "invoices"
    id = Column(Integer,primary_key=True)
    customer_id = Column(Integer,ForeignKey("customers.id"))
    date = Column(DATETIME,default=datetime.now())
    
    customer = relation(Customers,backref=backref("invoices") )
    products = relation("Products",secondary="invoice_product" )

class InvoiceProduct(Base):
    __tablename__ = "invoice_product"
    id = Column(Integer,primary_key=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    product_id = Column(Integer,ForeignKey("products.id"))
    quantity = Column(Integer, default=1)
