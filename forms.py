"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional, Email, DataRequired, URL


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired()] )
    photo_url = StringField('Photo URL', validators=[DataRequired(), URL()])
    age=SelectField("Age",
                    choices=[('baby','Baby'),
                             ('young','Young'),
                             ('adult','Adult'),
                             ('senior','Senior')],
                              validators=[InputRequired()])
    notes=StringField('Notes') //TODO: add validator

