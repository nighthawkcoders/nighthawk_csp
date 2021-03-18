from flask import Blueprint

y2021_tri3_bp = Blueprint('y2021_tri3', __name__,
                          template_folder='templates',
                          static_folder='static', static_url_path='assets')


@y2021_tri3_bp.route('/')
def index():
    return "Y2021 tri3 Home Site"
