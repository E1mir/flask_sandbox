from flask import render_template, redirect, url_for
from flask import request

from app_conf import app, db_session
from models import Comment


@app.route('/')
def index():
    comments = Comment.query.all()
    # another way to create and use context
    context = {
        'title': 'Index page',
        'page': 'index',
        'comments': comments
    }
    return render_template(
        'project/index.html',
        **context
    )


@app.route('/add_comment')
def add_comment():
    return render_template(
        'project/add_comment_form.html',
        title='Add comment page',
        page='add_comment'
    )


@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form['comment']
    # create a signature
    signature = Comment(name=name, comment=comment)
    # add it into database session then save it.
    db_session.add(signature)
    db_session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
