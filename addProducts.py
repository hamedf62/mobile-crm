from unicodedata import category, name
from models import Categories, Customers, Invoices, Products
from connection import dbsession

# newCategories = [{"name":"Smart phones"},{"name":"Headsets"},{"name":"Battery Chargers"}]
# newCustomers 
# newProducts = [{"name":"iphone","type":2022},{"name":"Samsung","type":"S22"}]

newCategory =[Categories(name="Smart phones"),Categories(name="Headsets"), Categories(name="Battery Chargers")]


newCustomers= Customers(fname="kiana", lname="kiazad", mobile="09120000000", email="kianakiazad74@gamil.com", password="1234", ncode=10, address="yazd,razmandegan ...")

newProducts= [Products(name="iphone", price=22.5), Products(name="samsung", price=15.5)]



dbsession.add_all(newCategory)
dbsession.add(newCustomers)
dbsession.add_all(newProducts)

dbsession.commit()