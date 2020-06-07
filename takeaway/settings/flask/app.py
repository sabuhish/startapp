app ='''
from app_init.app_factory import create_app
from flask import jsonify, current_app, request
from flask_jwt_extended import (
    jwt_required,
    create_access_token,
    get_jwt_identity,
    get_jwt_claims,
    create_refresh_token,
    jwt_refresh_token_required,
)
from marshmallow import ValidationError
from app.utils import verify_secret
import os
import warnings

warnings.simplefilter("ignore")

settings_name = os.getenv("settings")

app = create_app(settings_name)


@app.route("/", methods=["GET"])
def myfunc():
    return jsonify({"result": True})

'''