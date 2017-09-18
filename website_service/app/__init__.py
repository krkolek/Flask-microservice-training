"""Initiates Flask's application and implements site's endpoint."""


from flask import Flask, request, flash, render_template
from flask_pymongo import PyMongo
from wtforms import StringField, Form
from wtforms.validators import DataRequired, URL
from config import get_config


app = Flask(__name__)
mongo = PyMongo(app)
app.config.from_object(get_config())


with app.app_context():
    """Creates settings object in db if doesn't exist."""
    if mongo.db.settings.find_one() is None:
        mongo.db.settings.insert_one({'api_url': 'http://127.0.0.1:5001'})


class SettingsForm(Form):
    """Form for updates runtime editable settings."""
    api_url = StringField(validators=(DataRequired(), URL()))


@app.route("/", methods=['GET', 'POST'])
def home():
    """The only site in the application which allows to update settings and manage users.

    Adding, showing and removing users is realized via JavaScript and AJAX.
    Settings update is implemented in the function below.
    """
    form = SettingsForm(request.form, data=mongo.db.settings.find_one())
    print form.api_url.data, request.method
    if request.method == 'POST':
        if form.validate():
            mongo.db.settings.update_one({}, {'$set': {'api_url': form.api_url.data}})
            flash('Saved successfully', 'message')
        else:
            form.api_url.data = mongo.db.settings.find_one()['api_url']
            flash('Wrong URL format', 'error')
    return render_template('base.html', form=form)
