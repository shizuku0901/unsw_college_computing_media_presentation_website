from flask import Blueprint, render_template, request, redirect, url_for, session
from extensions import db

# create a Blueprint instance for the record page
record_bp = Blueprint('record', __name__)

# define a route for the record page
@record_bp.route(
    '/record',
    methods=['GET', 'POST']
)

# define the index function to render the record page
def index():

    # check if the user is logged in by checking if 'uid' is in the session
    if 'uid' not in session:
        # if the user is not logged in, redirect to the login page
        return redirect(url_for('auth.login'))
    
    # retrieve all activities from the database
    if request.method == 'POST':
        # retrieve the form data
        activity_name = request.form.get('activity_name')
        time = request.form.get('time')

        # add the new activity to the database
        db.collection('activities').add({
            'user_id': session['uid'],
            'activity_name': activity_name,
            'time': int(time)
        })

        return redirect(url_for('welcome.index'))

    #  render the record/index.html template with the retrieved activities
    return render_template('record/index.html')