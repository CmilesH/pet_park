from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Pet
from myapp.pets.forms import AddPetForm

pets = Blueprint('pets', __name__) # register this in __Init__ py 

# Create a blog post 

@pets.route('/add', methods=['GET', 'POST'])
@login_required
def add_pet():
    form = AddPetForm()
    if form.validate_on_submit():
        pets = Pet(name=form.name.data, breed=form.breed.data, image=form.image.data, user_id=current_user.id)
        db.session.add(pets)
        db.session.commit()
        flash('Pet Created')
        print('Pet was created')
        return redirect(url_for('core.pets'))
    return render_template('add_pet.html', form=form)