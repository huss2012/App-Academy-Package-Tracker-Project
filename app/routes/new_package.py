from flask import Blueprint, render_template, request, redirect
from ..forms.shipping_form import ShippingForm
from app.models import db, Package


bp = Blueprint("new_package", __name__, url_defaults="")

@bp.route("/new_package", methods=["GET", "POST"])
def new_package():
    shipping_form = ShippingForm()

    if shipping_form.validate_on_submit():
        data = shipping_form.data
        new_package = Package(sender= data['sender_name'],
                              recipient=data['recpient_name'],
                              origin=data['origin'],
                              destination=data['destination'],
                              location=data['origin']
                              )
        db.session.add(new_package)
        db.session.commit()
        Package.advance_all_locations()
        return redirect('/')


    return render_template("shipping_request.html", shipping_form = shipping_form)
