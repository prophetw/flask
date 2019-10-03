from flask import Flask, escape, url_for, request, render_template, make_response, abort
from flask_cors import CORS, cross_origin
import os;
app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template('hello.html'))
    resp.set_cookie('username', 'the username')
    return resp

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    username = request.cookies.get('username')
    return render_template('hello.html', name=username)

@app.route('/login', methods=['GET', 'POST'])
@cross_origin()
def login():
    if request.method == 'POST':
        return 'start login in'
    else:
        return 'show login form'

@app.route('/send-email', methods=['POST'])
@cross_origin()
def send_email():
    if request.method == 'POST':
        response = os.system('echo "hello pi" | mutt -s "api send email" 532300391@qq.com')
        return 'send email via python'
    else:
        return 'sendEmail'

@app.route('/projects/')
def projects():
    abort(401)

@app.route('/about')
def about():
    return 'The about page'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

@app.route("/me")
def me_api():

    return {
        "username": "321",
        "theme": "darg"
    }

with app.test_request_context():
    print(url_for('static', filename='style.css'))
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
