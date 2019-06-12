from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from flask_wtf.file import FileField, FileAllowed

app = Flask(__name__)  # class
# Location of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crudapp.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SECRET_KEY"] = "topsecret"
# creating the database
db = SQLAlchemy(app)


# db.create_all()- Activate the database
# db.drop_all()- Used to delete the entire database
# from app import db - Import the database inside  the TERMINAL
# fetching data from the database = languages.query.all()
# add data to the database = db.session.add(data)
# saving data in the database = db.session.commit()


# programming language table/model
class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    image = db.Column(db.String(60))
    description = db.Column(db.Text)

    def __repr__(self):
        return self.name


class LanguageForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired])
    description = TextAreaField('Description', validators=[DataRequired])
    image = FileField("Add Image", validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField("Add A Language")


# CRUD APP create ,read , update, delete

@app.route('/')
def index():  # function
    # fruits = ['Banana', 'Avocado', 'Apple', 'Mango']  # list type
    # return render_template('Index.html', the_fruits=fruits)
    languages = Language.query.all()
    return render_template('Index.html', languages=languages)


@app.route('/add_data', methods=["GET", "POST"])
def add_data():
    if request.method == "POST":
        # grabbing data from the submitted form
        name = request.form['firstname']
        description = request.form['description']
        image = request.form['image']
        # creating a language object using the language class
        new_language = Language(name=name, description=description, image=image)
        db.session.add(new_language)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template('add_data.html')


# READ DATA - CRUD


@app.route('/detail/<int:language_id>')
def detail_page(language_id):
    # fetching data from the database using the id
    lang = Language.query.filter_by(id=language_id).one()

    return render_template('detail.html', language=lang)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/about/<name>')
def greeting(name):
    name_length = len(name)
    return render_template("greetings.html", the_name=name, name_length=name_length)


@app.route('/contact_us')
def contact_us():
    return render_template("contact_us.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')


@app.route('/developer/<string:dev_id>')
def developer(dev_id):
    lang = "python"
    framework = "flask"
    return "My Id is {} and I code using {} and I also use {]".format(dev_id, lang, framework)


# @app.route('/create')
# def create():

if __name__ == '__main__':
    app.run(debug=True, port=3000)
