from flask import Blueprint, render_template
from algorithm.image import image_data
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

app_starter = Blueprint('starter', __name__,
                       url_prefix='/starter',
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='assets')


@app_starter.route('/binary/')
def binary():
    return render_template("starter/binary.html")


@app_starter.route('/rgb/')
def rgb():
    path = Path(app_starter.root_path) / "static" / "img"
    return render_template('starter/rgb.html', images=image_data(path))