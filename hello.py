from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/')
@app.route('/index')
@app.route("/hello_world")
def helloa():
    return 'Hello, World'


def index():
    return 'Index Page'


def hello_world():
    return "<p>Hello, World!</p>"