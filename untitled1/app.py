import flask

app = Flask(__name__)


@app.route('/')
def index():
    return flask.render_template()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
