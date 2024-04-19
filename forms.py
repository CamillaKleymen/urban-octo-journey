from flask_wtf import FlaskForm
from wtforms import (StringField, EmailField, PasswordField, SubmitField)

from wtforms.validators import DataRequired

# form for registration
class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Enter a name")])
    email = EmailField("email", validators=[DataRequired("Enter an email")])
    month = StringField("month", validators=[DataRequired("Enter a month and a day")])
    cardnum = PasswordField("cardnum", validators=[DataRequired("Enter a cardnum")])
    password = PasswordField("password", validators=[DataRequired("Enter a password")])

    button = SubmitField("Registrate")

class MovingoutForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired("Enter a name")])
    email = EmailField("email", validators=[DataRequired("Enter an email")])

    button = SubmitField("Sign in ")
