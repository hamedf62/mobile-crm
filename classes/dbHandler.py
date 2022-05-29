from models import *
from connection import Session


class DBHandler:
    def __init__(self) -> None:
        self.dbsession = Session()

    def addCustomer(self, customers):
        self.dbsession.bulk_insert_mappings(Customers, customers.to_dict(orient="records"))
        self.dbsession.flush()

    def addCategories(self, categories):
        self.dbsession.bulk_insert_mappings(Categories, categories.to_dict(orient="records"))
        self.dbsession.flush()