from flask import Blueprint
admin_bp = Blueprint("admin_bp",__name__,template_folder = "templates",url_prefix = "/admin")
