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
    pets = Pet.query.all()

    return render_template("index.html", pets=pets)

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

        pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes)

        db.session.add(pet)
        db.session.commit()

        flash(f"Added {name}")
        return redirect("/")

    else:
        return render_template("pet_add_form.html", form=form)

@app.route('/<int:pet_id_number>',methods=['GET','POST'])
def edit_show_pet(pet_id_number):
    """edit and show pet information """

    pet = Pet.query.get_or_404(pet_id_number) #TODO: always use _or_404!
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        pet.photo_url=pet.photo_url
        pet.notes=pet.notes
        pet.available=pet.available

        db.session.commit()

        flash(f"Edited {pet.photo_url} {pet.notes} {pet.available}")
        return redirect("/")

    else:
        return render_template("pet_info.html", form=form, pet=pet)

