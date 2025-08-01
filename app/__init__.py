from flask import Flask
from app.config import Config
from app.extensions import db, migrate
from app.routes import api


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(api)

    with app.app_context():
        from app import models

    return app
