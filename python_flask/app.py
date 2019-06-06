from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crudapp.sqlite3'
db = SQLAlchemy(app)


# db.create_all()- Activate the database
# db.drop_all()- Used to delete the entire database
# from app import db - Import the database inside  the TERMINAL

class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=True)
    image = db.Column(db.String(60))
    description = db.Column(db.Text)

    def __rep__(self):
        self.name


# CRUD APP create ,read , update, delete

@app.route('/')
def index():  # function
    # fruits = ['Banana', 'Avocado', 'Apple', 'Mango']  # list type
    # return render_template('Index.html', the_fruits=fruits)
    languages = Language.query.all()
    return render_template('Index.html', languages=languages)


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
