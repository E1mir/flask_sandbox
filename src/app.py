from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = {
        'hello': 'Hello from FLASK.PY'
    }
    return render_template('example/example.html', context=context)


@app.route('/home')
def home():
    return "<h1>You are on the home page!</h1>"


@app.route('/home/<string:place>')
def home_place(place):
    return f'<h1>You are on the {place}!</h1>'


@app.route('/some_post', methods=['POST'])
def post_request():
    return 'Hello from POST!'


@app.route('/get_post', methods=['GET', 'POST'])
def get_post_page():
    return "It works"


if __name__ == '__main__':
    app.run()
