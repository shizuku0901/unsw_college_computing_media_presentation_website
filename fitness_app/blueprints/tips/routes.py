from flask import Blueprint, render_template
from models.tip import Tip

# create a Blueprint instance for the tips page
tips_bp = Blueprint('tips', __name__)

# define a route for the tips page
@tips_bp.route('/tips')

# define the index function to render the tips page
def index():
    # retrieve all tips from the database
    tips = Tip.query.all()

    # render the tips/index.html template with the retrieved tips
    return render_template(
        'tips/index.html',
        tips = tips
    )