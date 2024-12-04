from flask import Blueprint, render_template, request, redirect
from ..forms.shipping_form import ShippingForm



bp = Blueprint("new_package", __name__, url_defaults="")

@bp.route("/new_package", methods=["GET", "POST"])
def new_package():
    shipping_form = ShippingForm()

    if shipping_form.validate_on_submit():
        print(f'{shipping_form.data}')
        return redirect('/new_package')


    return render_template("shipping_request.html", shipping_form = shipping_form)
