from flask import Blueprint, render_template

# create a Blueprint instance for the facility page
facility_bp = Blueprint('facility', __name__)

# define a route for the facility page
@facility_bp.route('/facility')

# define the index function to render the facility page
def index():
    # render the facility/index.html template
    return render_template('facility/index.html')