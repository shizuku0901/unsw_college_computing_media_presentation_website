from flask import Blueprint, render_template
from extensions import db

# create a Blueprint instance for the tips page
tips_bp = Blueprint('tips', __name__)

# define a route for the tips page
@tips_bp.route('/tips')

# define the index function to render the tips page
def index():
    # retrieve all tips from the database
    tips_ref = db.collection('tips')
    # convert the tips to a list of dictionaries
    tips = [doc.to_dict() for doc in tips_ref.stream()]

    # render the tips/index.html template with the retrieved tips
    return render_template(
        'tips/index.html',
        tips = tips
    )