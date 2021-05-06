from flask_wtf import FlaskForm
from wtforms import SubmitField, HiddenField
from wtforms import StringField, validators, SelectField, HiddenField

class CounterForm(FlaskForm):
    fatality_count = SelectField(u'Fatality Count', choices=[(i, i) for i in range(6)], coerce=int,
                                 render_kw={"class": "form-select", "form": "form"})

    infection_count = SelectField(u'Infection Count', choices=[(i, i) for i in range(6)], coerce=int,
                                    render_kw={"class": "form-select", "form": "form"})

    lat = HiddenField('lat', id="lat")
    long= HiddenField('long', id="long")
    submit = SubmitField(label="Submit", render_kw={"class": "btn btn-primary"})

    def __repr__(self):
        return f"c_type: {self.c_type.label}, submit: {self.submit}"

