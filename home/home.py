from flask import Blueprint, render_template

# import utilities.utilities as utilities


home_blueprint = Blueprint(
    'home_bp', __name__)


@home_blueprint.route('/', methods=['GET'])
def home():
    return render_template(
        'home/home.html'
        # selected_movies=utilities.get_selected_movies(),
        # tag_urls=utilities.get_tags_and_urls()
    )
