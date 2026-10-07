from datetime import date, timedelta
from extensions import db

def week_start():
    today = date.today()
    return (today - timedelta(days=today.weekday())).isoformat()  # 今週の月曜

def weekly_total(uid):
    start = week_start()
    docs = db.collection('activities').where('user_id', '==', uid).stream()
    total = 0
    for d in docs:
        data = d.to_dict()
        if data.get('date', '') >= start:
            total += data.get('time', 0)
    return total