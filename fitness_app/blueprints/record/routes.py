from flask import Blueprint, render_template, request, redirect, url_for
from models.activity import Activity
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

    # retrieve all activities from the database
    if request.method == 'POST':
        # retrieve the form data
        activity_name = request.form.get('activity_name')
        time = request.form.get('time')

        # create a new Activity object
        new_activity = Activity(
            user_id = 'user1',
            activity_name = activity_name,
            time = time
        )

        # add the new activity to the database
        db.session.add(new_activity)
        db.session.commit()

        # redirect to the welcome page after submission
        return redirect(url_for('welcome.index'))

    #  render the record/index.html template with the retrieved activities
    return render_template('record/index.html')