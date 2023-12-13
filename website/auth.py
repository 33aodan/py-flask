from flask import Blueprint, render_template
auth = Blueprint("auth", __name__)


@auth.route('/login')
def login():
    return render_template("login.html", name="Baodan", email="enter your email: ")


@auth.route('/logout')
def logout():
    return "<h1>Logout page</h1>"


@auth.route('/signup')
def signup():
    return render_template("signup.html", name="username", email="example@email.com")


@auth.route('/signout')
def signout():
    return "<h1>signout page</h1>"