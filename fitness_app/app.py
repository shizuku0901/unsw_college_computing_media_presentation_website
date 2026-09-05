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
        db.drop_all()  # Drop all tables (for development purposes)
        db.create_all()
        seed_data()

    return app

def seed_data():
    from models.tip import Tip

    if Tip.query.first():
        return

    tips = [
        Tip(
            published_date='2026-09-01',
            title='Importance of Stretching',
            detail='Stretching before and after exercise helps prevent injury and improves flexibility.',
            source='https://example.com/stretching'
        ),
        Tip(
            published_date='2026-09-03',
            title='Stay Hydrated',
            detail='Drink at least 2 liters of water per day, especially on exercise days.',
            source='https://example.com/hydration'
        ),
        Tip(
            published_date='2026-09-05',
            title='Rest Days Are Important',
            detail='Allow your body to recover by taking at least one rest day per week.',
            source='https://example.com/rest'
        ),
    ]
    for tip in tips:
        db.session.add(tip)
    db.session.commit()

if __name__ == '__main__':
    app = create_app()
    app.run(
        debug = True,
        port = 5001
    )

app = create_app()