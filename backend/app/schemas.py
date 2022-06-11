# from attr import field
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import Schema, EXCLUDE, fields
from db.models import *
from marshmallow_sqlalchemy import auto_field, SQLAlchemyAutoSchema


class ProductsSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Products
        load_instance = True  # Optional: deserialize to model instances
        include_fk = True

   
class UsersSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_instance = True
        load_only = ("password",)

    email = fields.Email()
    _password = auto_field(data_key="password", attribute="password")

    name = fields.Function(
        lambda obj: f"{obj.fname_fa} {obj.lname_fa}"
        if (obj.fname_fa or obj.lname_fa)
        else f"{obj.fname_en} {obj.lname_en}"
    )
