from flask import Blueprint, render_template

y2021_bp = Blueprint('y2021_repos', __name__,
                     url_prefix='/y2021',
                     template_folder='templates',
                     static_folder='static', static_url_path='/static/assets')


@y2021_bp.route('/repos')
def repos():
    return render_template("course/repos.html")
