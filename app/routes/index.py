from flask import Blueprint, render_template
from app.models import db, Package

bp = Blueprint("index", __name__, url_defaults="")

@bp.route("/", methods=["GET", "POST"])
def index():
    packages = Package.query.all()

    if packages:
        return render_template("package_status.html", packages=packages)

    return render_template("index.html")
