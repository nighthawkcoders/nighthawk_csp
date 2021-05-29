from flask import Blueprint, render_template

y2021_tri2_bp = Blueprint('y2021_tri2', __name__,
                          url_prefix='/y2021/tri2',
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@y2021_tri2_bp.route('/')
def index():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/cspcbproject")
