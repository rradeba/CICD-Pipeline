from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from schemas.sum_schema import ma
from models.sum import Base
from routes.sum_routes import sum_bp

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    ma.init_app(app)


    with app.app_context():
        db.create_all()

    
    app.register_blueprint(sum_bp)

    return app
