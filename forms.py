"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,BooleanField
from wtforms.validators import InputRequired, Optional, URL


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('cat','Cat'), #FIXME: have variables at top (list)
                                              ('dog','Dog'),
                                              ('porcupine','Porcupine')],
                                              validators=[InputRequired()] )
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age=SelectField("Age",
                    choices=[('baby','Baby'),
                             ('young','Young'),
                             ('adult','Adult'),
                             ('senior','Senior')],
                              validators=[InputRequired()])
    notes=StringField('Notes') #FIXME: textarea

class EditPetForm(FlaskForm):
    """form for editing pets"""
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    notes=StringField('Notes')
    available=BooleanField('Available')#TODO:  add validator