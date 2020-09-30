"""
Admin routes
"""
from flask import Blueprint, render_template, current_app


api = Blueprint("admin", __name__, template_folder='templates', static_folder='static')


@api.route("/<key>")
def home(key):
    """ main admin page """
    admin_key = current_app.config["ADMIN_KEY"]
    if admin_key == key:
        return render_template('admin/index.html')
    return '{"status":"Cannot connect to service"}'
