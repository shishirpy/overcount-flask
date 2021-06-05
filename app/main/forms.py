from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField
from wtforms import StringField, validators, SelectField, HiddenField
from wtforms.validators import DataRequired

class CounterForm(FlaskForm):
    fatality_count = SelectField(u'Fatality Count', choices=[(i, i) for i in range(3)], coerce=int,
                                 render_kw={"class": "form-control form-select", "form": "form"})

    infection_count = SelectField(u'Infection Count', choices=[(i, i) for i in range(6)], coerce=int,
                                    render_kw={"class": "form-control form-select", "form": "form"})

    lat = HiddenField('lat', id="lat")#, validators=[DataRequired()])
    long= HiddenField('long', id="long")#, validators=[DataRequired()])
    country = SelectField(u'Country', choices=[("INDIA", "INDIA"), ("NEPAL", "NEPAL")], 
                validators=[DataRequired()], render_kw={"class": "form-control form-select"})
    zipcode = StringField(u'Pin Code', render_kw = {"class": "form-control"})
    submit = SubmitField(label="Submit", render_kw={"class": "btn btn-primary form-control"})
