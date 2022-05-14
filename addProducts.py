from unicodedata import name
from models import Categories, Products
from connection import dbsession

# newCategories = [{"name":"Smart phones"},{"name":"Headsets"}]

# newProducts = [{"name":"iphone","type":2022},{"name":"Samsung","type":"S22"}]

newCategory = Categories(name="Smart phones")




dbsession.add(newCategory)

dbsession.commit()