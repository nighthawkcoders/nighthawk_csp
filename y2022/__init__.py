from flask import Blueprint, render_template

y2022_bp = Blueprint('y2022', __name__,
                     url_prefix='/y2022',
                     template_folder='templates',
                     static_folder='static', static_url_path='/static/assets')


@y2022_bp.route('/repos')
def repos():
    return render_template("course/repos.html")

@y2022_bp.route('/padlet')
def padlet():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/csp2022tri1")
