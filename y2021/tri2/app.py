from flask import Blueprint

y2021_tri2_bp = Blueprint('y2021_tri2', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@y2021_tri2_bp.route('/')
def index():
    return "Y2021 tri2 Home Site"
