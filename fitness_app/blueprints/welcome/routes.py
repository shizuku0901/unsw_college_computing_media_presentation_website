from flask import Blueprint, render_template, session, redirect, url_for
from extensions import db

# create a Blueprint instance for the welcome page
welcome_bp = Blueprint('welcome', __name__)

# define a route for the welcome page
@welcome_bp.route('/')
# define the index function to render the tips page
def index():
    # check if the user is logged in by checking if 'uid' is in the session
    if 'uid' not in session:
        # if the user is not logged in, redirect to the login page
        return redirect(url_for('auth.login'))
    # if the user is logged in, retrieve the user's information from the database
    uid = session['uid']
    # retrieve the user document from the database using the uid
    user_doc = db.collection('users').document(uid).get()
    # convert the user document to a dictionary if it exists, otherwise set user to None
    user = user_doc.to_dict() if user_doc.exists else None
    # retrieve all activities for the logged-in user from the database
    activities_ref = db.collection('activities').where('user_id', '==', uid)
    # convert the activities to a list of dictionaries
    activities = [doc.to_dict() for doc in activities_ref.stream()]
    # calculate the total time spent on activities
    total_time = sum([a['time'] for a in activities])

    # render the welcome/index.html template with the retrieved activities and total time
    return render_template(
        'welcome/index.html',
        user = user,
        total_time = total_time
    )

