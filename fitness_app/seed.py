from extensions import db

tips = [
    {
        'published_date': '2026-09-01',
        'title': 'Importance of Stretching',
        'detail': 'Stretching before and after exercise helps prevent injury and improves flexibility.',
        'source': 'https://example.com/stretching'
    },
    {
        'published_date': '2026-09-03',
        'title': 'Stay Hydrated',
        'detail': 'Drink at least 2 liters of water per day, especially on exercise days.',
        'source': 'https://example.com/hydration'
    },
    {
        'published_date': '2026-09-05',
        'title': 'Rest Days Are Important',
        'detail': 'Allow your body to recover by taking at least one rest day per week.',
        'source': 'https://example.com/rest'
    },
]

for tip in tips:
    db.collection('tips').add(tip)

print('Done!')