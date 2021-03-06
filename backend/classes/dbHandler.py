from db.models import *
from db.connection import Session, Base, engine



class DBHandler:
    def __init__(self) -> None:
        self.dbsession = Session()

    def create_all_tables(self):
        Base.metadata.create_all(engine)

    def addUser(self, users):
        self.dbsession.bulk_insert_mappings(Users, users.to_dict(orient="records"))
        self.dbsession.flush()

    # def addCategories(self, categories):
    #     self.dbsession.bulk_insert_mappings(Categories, categories.to_dict(orient="records"))
    #     self.dbsession.flush()

    def addProducts(self, products):
        self.dbsession.bulk_insert_mappings(Products, products.to_dict(orient="records"))
        self.dbsession.flush()