from flask import Blueprint, render_template
from extensions import db

# create a Blueprint instance for the welcome page
welcome_bp = Blueprint('welcome', __name__)

# define a route for the welcome page
@welcome_bp.route('/')
# define the index function to render the tips page
def index():
    # retrieve all activities from the database
    activities_ref = db.collection('activities')
    # convert the activities to a list of dictionaries
    activities = [doc.to_dict() for doc in activities_ref.stream()]
    # calculate the total time spent on activities
    total_time = sum([a['time'] for a in activities])

    # render the welcome/index.html template with the retrieved activities and total time
    return render_template(
        'welcome/index.html',
        total_time = total_time
    )

