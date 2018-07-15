from .... import db

class Menu(db.Model):
    __tablename__ = 'menus'

    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(120), unique=True, nullable=False)
    parent = db.Column(db.Integer)