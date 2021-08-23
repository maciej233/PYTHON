from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_httpauth import HTTPBasicAuth


db = SQLAlchemy()
DB_NAME = 'database.db'

authorization = HTTPBasicAuth()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'MY_SECRET_KEY_1234'
    app.config['SQLAlCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .sites import sites
    from .auth import auth

    app.register_blueprint(sites, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .models import Device
    create_databse(app)
        
    return app

def create_databse(app):
    if not os.path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Succesfully created databse')