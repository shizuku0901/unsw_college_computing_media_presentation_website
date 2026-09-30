from flask import Blueprint, render_template, session, redirect, url_for

facility_bp = Blueprint('facility', __name__)

@facility_bp.route('/facility')
def index():
    # Redirect to login page if not logged in
    if 'uid' not in session:
        return redirect(url_for('auth.login'))

    return render_template('facility/index.html')