from flask import Blueprint, render_template, request, redirect, url_for, session
from extensions import db
from utils import week_start, weekly_total

goal_bp = Blueprint('goal', __name__)

@goal_bp.route('/goal', methods=['GET', 'POST'])
def index():
    if 'uid' not in session:
        return redirect(url_for('auth.login'))

    uid = session['uid']
    ref = db.collection('goals').document(uid)

    if request.method == 'POST':
        try:
            minutes = int(request.form.get('weekly_minutes'), 0)
        except ValueError:
            minutes = 0
        if 1 <= minutes <= 3000:
            ref.set({'weekly_minutes': minutes})
        return redirect(url_for('goal.index'))

    snap = ref.get()
    target = snap.to_dict().get('weekly_minutes') if snap.exists else None
    done = weekly_total(uid)
    percent = min(100, done * 100 / target) if target else 0
    return render_template('goal/index.html', target=target, done=done, percent=percent)