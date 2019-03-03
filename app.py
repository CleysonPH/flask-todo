import os
from flask import Flask

from models import db
import views


def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    views.configure(app)

    return app


if __name__ == "__main__":
    app = create_app()

    app.run(debug=True)
    