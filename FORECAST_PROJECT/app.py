import flask
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, ValidationError, Length, Email, EqualTo
from flask_wtf.file import FileField, FileAllowed
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from flask_mail import Message, Mail
from flask_bcrypt import Bcrypt
import os

UPLOAD_FOLDER = '/static/upload/'
# ALLOWED_EXTENSIONS = set(['pdf'])

app = flask.Flask(__name__, instance_relative_config=True)  # class
bootstrap = Bootstrap(app)
basedir = os.path.abspath(os.path.dirname(__file__))
# Location of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crudapp.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "topsecret"

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config["MAIL_SERVER"] = "smtp.googlemail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
mail = Mail(app)
bcrypt = Bcrypt(app)
# creating the database
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_title = db.Column(db.String(50), unique=True, nullable=False)
    product_picture = db.Column(db.String(60))
    product_content = db.Column(db.Text)
    product_price = db.Column(db.Text)

    def __repr__(self):
        return self.product_title


class ProductForm(FlaskForm):
    product_title = StringField("Title", validators=[DataRequired()])
    product_picture = FileField('Product picture', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    product_content = TextAreaField("Description", validators=[DataRequired()])
    product_price = StringField("Price", validators=[DataRequired()])
    submit = SubmitField("New Product")


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    subject = StringField("Subject", validators=[DataRequired()])
    message = TextAreaField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")


class User(UserMixin, db.Model):
    __table_name__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_username = db.Column(db.String(50))
    user_email = db.Column(db.String(50))
    user_password = db.Column(db.String(50))
    user_about_me = db.Column(db.String(50))
    # products = db.Column(db.String(50))
    user_tech_stack = db.Column(db.String(50))
    user_skills = db.Column(db.String(200))
    user_experience = db.Column(db.Text())
    user_publication = db.Column(db.String(50))
    # user_products = db.relationship('Product', backref='author', lazy='dynamic')


class UserForm(FlaskForm):
    user_username = StringField("Username", validators=[DataRequired(), Length(min=4, max=50)])
    user_email = StringField("email", validators=[DataRequired(), Email(message="Invalid email address")])
    user_password = PasswordField("Password", validators=[DataRequired(), EqualTo("confirm"), Length(min=5, max=100)])
    confirm = PasswordField("Confirm")
    submit = SubmitField("Signup")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("User with the credentials exists")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("User with the credentials exists")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email(message="Invalid email address")])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=5, max=80)])
    submit = SubmitField()


class EditUserForm(FlaskForm):
    about_me = TextAreaField("About me", validators=[DataRequired()])
    tech_stack = StringField("Tech Stack", validators=[DataRequired()])
    # products = StringField("Projects", validators=[DataRequired()])
    publication = StringField("Publications", validators=[DataRequired()])
    skills = StringField("Skills", validators=[DataRequired()])
    experience = TextAreaField("Experience", validators=[DataRequired()])
    submit = SubmitField()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    products = Product.query.all()
    return flask.render_template('index.html', products=products)


@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product_detail(product_id):
    product = Product.query.filter_by(id=product_id).first()
    form = ProductForm()
    if form.validate_on_submit():
        if form.product_picture.data:
            f = form.product_picture.data
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.root_path + "/static/images/imgs", filename))
            path = url_for('static', filename='images/imgs/'+ filename)
            product_picture = str(path)

        product.title = form.product_title.data
        product.content = form.product_content.data

        db.session.add(product)
        db.session.commit()
        flask.flash('Product updated successfully', 'success')
        return flask.redirect(flask.request.url)

    form.product_title.data = product.product_title
    form.product_picture.data = product.product_picture
    form.product_content.data = product.product_content
    form.product_price.data = product.product_price

    return flask.render_template('product_page.html', product=product, form=form)

def save_picture(form_picture):
    _, f_ext = os.path.splitext(form_picture.filename)
    pic_name = _ + f_ext
    print(pic_name)
    picture_path = os.path.join(app.root_path + "/static/imgs/profile_imgs", pic_name)
    form_picture.save(picture_path)
    return pic_name


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        if form.product_picture.data:
            print("helo")
            picture = save_picture(form.product_picture.data)
            filename = secure_filename(picture.filename)
            print(filename)
            picture.save(os.path.join(app.root_path + "/static/images/imgs", filename))
            path = url_for('static', filename='images/imgs/' + filename)
            product_picture = str(path)
            print(picture)
            product_title = form.product_title.data
            product_content = form.product_content.data
            product_price = form.product_price.data

            product = Product(product_title=product_title, product_content=product_content, product_price=product_price)
            db.session.add(product)
            db.session.commit()
            flask.flash("Product addition successful", "Success")
            return flask.redirect(flask.url_for("index", product_id=product.id, form=form))
        else:
            product_title = form.product_title.data
            product_content = form.product_content.data
            product_price = form.product_price.data
            product = Product(product_title=product_title, product_content=product_content, product_price=product_price)
            db.session.add(product)
            db.session.commit()
            flask.flash("Product addition successful", "Success")
            return flask.redirect(flask.url_for("index", product_id=product.id))
    return flask.render_template("add_product.html", form=form, title="Adding Sale")


# USER PROFILE SYSTEM
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    admin = User.query.filter_by(username='admin').first()
    user = User.query.filter_by(username='current_user.username').first()
    return flask.render_template("profile.html", admin=admin, user=user)


@app.route('/profile/edit/', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditUserForm()
    if form.validate_on_submit():
        current_user.about_me = form.about_me.data
        current_user.tech_stack = form.tech_stack.data
        # current_user.projects = form.projects.data
        current_user.skills = form.skills.data
        current_user.experience = form.experience.data
        current_user.publication = form.publication.data

        db.session.commit()
        flask.flash("Update success")
        return flask.render_template('profile.html', user=current_user)

    form.about_me.data = current_user.about_me
    form.tech_stack.data = current_user.tech_stack
    # form.products.data = current_user.projects
    form.skills.data = current_user.skills
    form.experience.data = current_user.experience
    form.publication.data = current_user.publication
    return flask.render_template('edit_profile.html', form=form, title="Edit profile")


# USER REGISTRATION SYSTEM
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = UserForm()
    if form.validate_on_submit():
        username = form.user_username.data
        email = form.user_email.data
        password = bcrypt.generate_password_hash(form.user_password.data).decode("utf-8")

        new_user = User(user_username=username, user_email=email, user_password=password)
        db.session.add(new_user)
        db.session.commit()
        flask.flash("Registration successful")
        return flask.redirect(flask.url_for('login'))

    return flask.render_template("register.html", form=form, title="Registration page")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_email=form.email.data).first()
        if user:
            if bcrypt.check_password_hash(user.user_password, form.password.data):
                login_user(user)
                flask.flash('Login successful')
                return flask.redirect(flask.url_for('index'))
            else:
                flask.flash('Password not correct')
                return flask.redirect(flask.url_for('login'))
        else:
            flask.flash('No user found')
            return flask.redirect(flask.url_for('login'))
    return flask.render_template("login.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    flask.flash('Welcome back again')
    return flask.redirect(flask.url_for('index'))


@app.route('/contact', methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message(form.subject.data, sender=form.email.data, recipients=['wkwabuiya2@gmail.com'])
        msg.body = """From: %s <%s> %s""" % (form.name.data, form.email.data, form.message.data)
        mail.send(msg)

        flask.flash("Message sent successfully", "success")
        return flask.redirect(flask.url_for("contact"))
    return flask.render_template('contact.html', form=form, title="Contact", )


@app.errorhandler(404)
def page_not_found(e):
    return flask.render_template("404.html"), 404


@app.errorhandler(500)
def internal_server_error(e):
    return flask.render_template('500.html'), 500


# @app.route('/create')
# def create():

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=4500)
