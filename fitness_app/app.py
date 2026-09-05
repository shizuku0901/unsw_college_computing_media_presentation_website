from flask import Flask
from config import Config
from extensions import db

# Initialize the Flask application
def create_app():

    app = Flask(
        __name__,
        template_folder = 'template',
        static_folder = 'statistic'
    )
    app.config.from_object(Config)

    # Initialize the database
    db.init_app(app)

    # Register blueprints
    from blueprints.welcome import welcome_bp
    from blueprints.tips import tips_bp
    from blueprints.facility import facility_bp
    from blueprints.record import record_bp

    app.register_blueprint(welcome_bp)
    app.register_blueprint(tips_bp)
    app.register_blueprint(facility_bp)
    app.register_blueprint(record_bp)

    # create the database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(
        debug = True,
        port = 5001
    )