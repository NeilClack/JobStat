from flask import Flask
from .extensions import db
from flask_marshmallow import Marshmallow
import os



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_mapping({
            'SQLALCHEMY_DATABASE_URI' : os.getenv('POSTGRES_DB_URI'),
            'SECRET_KEY' : "sdfghjiuytrewsdfvghjuytrewsdfghytredcvbhytredcvbhytre",
            "JSONIFY_PRETTYPRINT_REGULAR" : True
        })
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Initialize the database
    db.init_app(app)
    # Initialize Marshmallow
    from .extensions import ma
    ma.init_app(app)

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        print(app.config['SECRET_KEY'])
        return 'Hello, World!'

    with app.app_context():

        from . import jobs
        app.register_blueprint(jobs.bp)
    
    return app