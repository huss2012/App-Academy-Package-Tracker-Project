from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired
from map.map import map

def generate_choices(data, value):
    choices = [(f'Chose {value}', f'Chose {value}')] + [(values, key) for key, values in data.items()]
    return choices


class ShippingForm(FlaskForm):
    sender_name = StringField("Sender Name",render_kw={"placeholder": "Sender name!"} ,validators=[DataRequired()])
    recpient_name = StringField("Recipient Name", render_kw={"placeholder": "Recpient name!"} , validators=[DataRequired()])
    origin = SelectField("Origin",choices=generate_choices(map, "origin") , validators=[DataRequired()])
    destination = SelectField("Destination", choices=generate_choices(map, "destination") , validators=[DataRequired()])
    express = BooleanField("Express", default=False)
    shipe = SubmitField("Ship")
