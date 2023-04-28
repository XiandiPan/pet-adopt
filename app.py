"""Flask app for adopt app."""

import os

from flask import Flask,render_template, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db,db,Pet
from forms import AddPetForm,EditPetForm


app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///adopt")

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get("/")
def homepage():
    """show homepage links"""


    return render_template("index.html")

@app.route('/add',methods=['GET','POST'])
def add_pet():
    """Pet add form; handle adding"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        flash(f"Added {name}")
        return redirect("/add")

    else:
        return render_template("pet_add_form.html", form=form)

@app.route('/<int:pet_id_number>',methods=['GET','POST'])
def edit_show_pet():
    """edit and show pet information """

    form = EditPetForm()

    if form.validate_on_submit():
        photo_url = form.photo_url.data
        notes = form.notes.data
        available = form.available.data

