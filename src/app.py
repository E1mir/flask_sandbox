from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hey there! I\'m using a Flask!</h1>'


@app.route('/home')
def home():
    return "<h1>You are on the home page!</h1>"


@app.route('/home/<string:place>')
def home_place(place):
    return '<h1>You are on the ' + place + '</h1>'


@app.route('/some_post', methods=['POST'])
def post_request():
    return 'Hello from POST!'


@app.route('/get_post', methods=['GET', 'POST'])
def get_post_page():
    return "It works"


if __name__ == '__main__':
    app.run()
