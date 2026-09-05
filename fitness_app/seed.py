from app import create_app
from extensions import db
from models.tip import Tip

app = create_app()

with app.app_context():

    # Delete all existing tips from the database
    Tip.query.delete()

    # Add new sample tips to the database
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

    db.session.add_all(tips)
    db.session.commit()
    print('Done')
