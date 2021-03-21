from flask import Blueprint

y2021_tri1_bp = Blueprint('y2021_tri1', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@y2021_tri1_bp.route('/')
def index():
    return "Y2021 tri1 Home Site"
