from flask import Blueprint, render_template, request, redirect, url_for, session
from extensions import db
from utils import week_start, weekly_total, new_share_id

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

@goal_bp.route('/goal/share', methods=['POST'])
def share():
    if 'uid' not in session:
        return redirect(url_for('auth.login'))
    ref = db.collection('goals').document(session['uid'])
    snap = ref.get()
    data = snap.to_dict() if snap.exists else {}
    if not data.get('share_id'):
        ref.set({'share_id': new_share_id()}, merge=True)
    return redirect(url_for('goal.index'))

@goal_bp.route('/goal/unshare', methods=['POST'])
def unshare():
    if 'uid' not in session:
        return redirect(url_for('auth.login'))
    from google.cloud.firestore import import DELETE_FIELD
    db.collection('goals').document(session['uid']).update({'share_id': DELETE_FIELD})
    return redirect(url_for('goal.index'))

@goal_bp.route('/goal/<share_id>')
def shared(share_id):
    docs = list(db.collection('goals').where('share_id', '==', share_id).limit(1).stream())
    if not docs:
        abort(404)
    goal_doc = docs[0]
    owner_uid = goal_doc.id
    target = goal_doc.to_dict().get('weekly_minutes')

    done = weekly_total(owner_uid)
    percent = min(100, done * 100 / target) if target else 0

    return render_template('goal/shared.html', target=target, done=done, percent=percent)

