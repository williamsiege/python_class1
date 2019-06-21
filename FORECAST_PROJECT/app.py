import flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Length, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user

import os
import datetime

app = flask.Flask(__name__)  # class
bootstrap = Bootstrap(app)
basedir = os.path.abspath(os.path.dirname(__file__))
# Location of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crudapp.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "topsecret"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
# creating the database
db = SQLAlchemy(app)


class User(UserMixin, db.Model):
    __table_name__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))
    about_me = db.Column(db.String(50))
    # projects = db.Column(db.String(50))
    tech_stack = db.Column(db.String(50))
    skills = db.Column(db.String(200))
    experience = db.Column(db.Text())
    publication = db.Column(db.String(50))
    projects = db.relationship('Project', backref='author', lazy='dynamic')


class UserForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=50)])
    email = StringField("email", validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField("Password", validators=[DataRequired(), EqualTo("confirm"), Length(min=8, max=80)])
    confirm = PasswordField("Confirm")
    submit = SubmitField()


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8, max=80)])
    submit = SubmitField()


@app.route('/')
def index():
    return flask.render_template('index.html')


# USER REGISTRATION SYSTEM
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = generate_password_hash(form.password.data, method="sha256")

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        flask.flash("Registration successful")
        return flask.redirect(flask.url_for('index'))

    return flask.render_template("register.html", form=form, title="Registration page")


@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return flask.render_template('500.html'), 500


# @app.route('/create')
# def create():

if __name__ == '__main__':
    app.run(debug=True, port=3000)
