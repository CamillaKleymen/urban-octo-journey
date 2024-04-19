from flask import Blueprint, render_template
from forms import RegisterForm, MovingoutForm
#create an object of component
user_bp = Blueprint('user', __name__, url_prefix="/user")

@user_bp.route("/")
def user():
    registration_link = "<a href='/user/registration'> Регистрация </a><br>"
    login_link = "<a href='/user/login'> Вход в аккаунт </a><br>"
    return "Hello from user"
@user_bp.route("/registration")
def registration():
    form = RegisterForm()
    return render_template("register.html", form=form)
@user_bp.route("/movingout")
def movingout():
    form = MovingoutForm()
    return render_template("movingout.html", form=form)