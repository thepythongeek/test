import os
from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_pyfile('config.py', silent=True)

    os.makedirs(app.config['UPLOADS_FOLDER'], exist_ok=True)

    from app.main import bp
    app.register_blueprint(bp)
    return app
