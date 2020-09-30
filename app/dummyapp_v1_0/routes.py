"""
Demo app
"""
from flask import Blueprint, jsonify

api = Blueprint("dummyapp_v1_0", __name__)


@api.route("/")
def home():
    """ test api """
    msg = "V1.0.0!!"
    return jsonify(
        message=msg
    )
