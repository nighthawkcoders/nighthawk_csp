from flask import Blueprint, render_template

y2021_tri1_bp = Blueprint('y2021_tri1', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@y2021_tri1_bp.route('/')
def index():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/csptime1_2")

