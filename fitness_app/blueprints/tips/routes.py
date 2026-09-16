from flask import Blueprint, render_template
from extensions import db

# create a Blueprint instance for the tips page
tips_bp = Blueprint('tips', __name__)

# define a route for the tips page
@tips_bp.route('/tips')

# define the index function to render the tips page
def index():

    tips_ref = db.collection('tips')
    tips = [doc.to_dict() for doc in tips_ref.stream()]

    return render_template(
        'tips/index.html',
        tips = tips
    )