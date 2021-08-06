from flask import Blueprint, render_template

starter_bp = Blueprint('starter', __name__,
                       url_prefix='/starter',
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='assets')


@starter_bp.route('/rgb', methods=["GET", "POST"])
def rgb():
    return render_template('starter/rgb.html')


@starter_bp.route('/binary/')
def binary():
    return render_template("starter/binary.html")
