from db.models import *
from db.connection import Session


class DBHandler:
    def __init__(self) -> None:
        self.dbsession = Session()

    def addUser(self, users):
        self.dbsession.bulk_insert_mappings(Users, users.to_dict(orient="records"))
        self.dbsession.flush()

    def addCategories(self, categories):
        self.dbsession.bulk_insert_mappings(Categories, categories.to_dict(orient="records"))
        self.dbsession.flush()