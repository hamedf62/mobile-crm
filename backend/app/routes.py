
from flask import jsonify, request, session
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    unset_jwt_cookies,
    jwt_required,
)
from .schemas import UsersSchema
import bcrypt
from flask import Flask, jsonify, Blueprint
from ..db.connection import Session
from ..db.models import *
import pandas as pd

blueprint = Blueprint(
    "api",
    __name__,
)

def mkresp(data=None, meta=None, type=202, **kwargs):
    output = {}
    if data:
        output["data"] = data
    if meta:
        output["meta"] = meta
    if kwargs:
        for key, value in kwargs.items():
            output[key] = value

    return jsonify(output), type


def login(user):
    additional_claims = UsersSchema(many=False).dump(user)
    access_token = create_access_token(identity=additional_claims)
    refresh_token = create_refresh_token(identity=additional_claims)
    return access_token, refresh_token


@blueprint.route("auth/login", methods=["POST"])
def local_login():
    data = request.json
    email = data.get("email")
    password = data.get("password")

    if (not email) | (not password):
        return mkresp(
            meta={"message": "email or password missed"},
            type=401,
        )

    db = DB("system")
    user = db.getUserInfo(email=email)

    if not user:
        return mkresp(
            meta={"message": "user not found."},
            type=401,
        )

    else:
        if not bcrypt.checkpw(password.encode("utf-8"), user._password):
            return mkresp(
                meta={
                    "message": "password is incorrect.",
                    "errors": {"password": ["wrong password"]},
                },
                type=401,
            )

    access_token, refresh_token = login(user)

    return mkresp(
        meta={
            "message": "Successfull Login",
            "access_token": access_token,
            "refresh_token": refresh_token,
        },
        type=202,
    )


@blueprint.route("auth/user", methods=["GET"])
@jwt_required()
def user():
    identity = get_jwt_identity()
    db = DB("system")
    user = db.getUserInfo(id=identity["id"])
    additional_claims = UsersSchema(many=False).dump(user)
    return mkresp(data=additional_claims)


@blueprint.route("auth/logout", methods=["POST"])
# @jwt_required()
def logout():
    response = jsonify({"msg": "logout successful"})
    session.clear()
    unset_jwt_cookies(response)

    return response


@blueprint.route("auth/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity()
    access_token = create_access_token(identity)
    return mkresp(meta={"access_token": access_token}, type=202)


@blueprint.route("products")
# @jwt_required()
def products():

    # mydata = [{"name":"apple","type":13},{"name":"Samsung","type":"S20"},{"name":"Shiaomy","type":100}]

    dbsession = Session()
    allProducts = dbsession.query(Products)
    allProducts = pd.read_sql(allProducts.statement, dbsession.connection())
    # print(allProducts)
    allProducts = allProducts.to_dict(orient="records")

    return mkresp(data=allProducts)

@blueprint.route("users")
def users():

    dbsession = Session()
    allUsers = dbsession.query(Users)
    allUsers = pd.read_sql(allUsers.statement, dbsession.connection())
    allUsers = allUsers.to_dict(orient="records")

    return mkresp(data=allUsers)
