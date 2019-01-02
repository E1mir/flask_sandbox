from app_conf import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    comment = db.Column(db.String(1000), nullable=False)
