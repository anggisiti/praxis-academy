from Flask import Flask, url_for, request 
from markupsafe import escape

app = Flask(__nama__)

@app.route('/')
def index():
    return "index"

@app.route('/login')
def login():
    print(request.method)
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}'\
