import os

from flask import Flask, render_template

from . import db
from .views import auth


def create_app(test_config=None):
    # create and configure app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='big secret',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load instance config if not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    # init db
    db.init_app(app)

    @app.route('/')
    def index():
        return render_template('base.html')

    # register blueprints
    app.register_blueprint(auth.bp) 
    app.add_url_rule('/', endpoint='index')

    return app
