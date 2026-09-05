from flask import Blueprint, render_template
from models.activity import Activity

# create a Blueprint instance for the welcome page
welcome_bp = Blueprint('welcome', __name__)

# define a route for the welcome page
@welcome_bp.route('/')
# define the index function to render the tips page
def index():
    # calculate the total time spent on activities
    total_time = sum([a.time for a in Activity.query.all()])

    # render the welcome/index.html template with the retrieved tips
    return render_template(
        'welcome/index.html',
        total_time = total_time
    )

