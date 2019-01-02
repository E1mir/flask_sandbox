from flask import render_template, redirect, url_for
from flask import request

from app_conf import app, db_session
from models import Comment


@app.route('/')
def index():
    comments = Comment.query.all()
    return render_template('project/index.html', title='Index page', page='index', comments=comments)


@app.route('/add_comment')
def add_comment():
    return render_template('project/add_comment_form.html', title='Add comment page', page='add_comment')


@app.route('/example')
def example():
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


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    signature = Comment(name=name, comment=comment)
    db_session.add(signature)
    db_session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
