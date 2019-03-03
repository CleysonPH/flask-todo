from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    date = db.Column(db.Date, nullable=False)
    priority = db.Column(db.String(10), nullable=False)

    
    def __init__(self, title, date, priority):
        self.title = title
        self.date = date
        self.priority = priority

    
    def __repr__(self):
        return '<Todo {}>'.format(self.title)
