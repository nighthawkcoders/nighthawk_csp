from flask import Blueprint, render_template

starter_bp = Blueprint('starter', __name__,
                       url_prefix='/starter',
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='assets')

@starter_bp.route('/binary/')
def binary():
    return render_template("starter/binary.html")


@starter_bp.route('/rgb', methods=["GET", "POST"])
def rgb():
    colors = [
        {'label': "black", 'file': "black-square.png"},
        {'label': "red", 'file': "red-square.png"},
        {'label': "green", 'file': "green-square.png"},
        {'label': "blue", 'file': "blue-square.png"},
        {'label': "white", 'file': "white-square.png"}
    ]
    return render_template('starter/rgb.html', colors=colors)
