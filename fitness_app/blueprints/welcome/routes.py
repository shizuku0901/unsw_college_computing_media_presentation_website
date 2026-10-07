from flask import Blueprint, render_template, session, redirect, url_for
from extensions import db
from datetime import date

welcome_bp = Blueprint('welcome', __name__)


@welcome_bp.route('/')
def index():
    if 'uid' not in session:
        return redirect(url_for('auth.login'))
    
    uid = session['uid']
    user_doc = db.collection('users').document(uid).get()
    user = user_doc.to_dict() if user_doc.exists else None

    today = date.today().isoformat()

    activities_ref = db.collection('activities').where('user_id', '==', uid)
    activities = [doc.to_dict() for doc in activities_ref.stream()]

    total_time = sum(
        a.get('time', 0) for a in activities if a.get('date') == today
    )

    return render_template(
        'welcome/index.html',
        user = user,
        total_time = total_time
    )

