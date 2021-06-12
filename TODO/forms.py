from flask_wtf import FlaskForm
from wtforms.validators import *
from wtforms import *


class TodoForm(FlaskForm):
    description = TextAreaField("Opis", validators=[DataRequired()])
    title = StringField("Nazwa", validators=[DataRequired()])
    done = BooleanField("Wykonake")