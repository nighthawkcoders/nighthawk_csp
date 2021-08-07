from flask import Blueprint, render_template
from PIL import Image
import numpy as np

starter_bp = Blueprint('starter', __name__,
                       url_prefix='/starter',
                       template_folder='templates',
                       static_folder='static',
                       static_url_path='assets')


def color_data(path="starter/static/"):  # path of blueprint run is default
    # prefill with label and file
    color_dict = [
        {'label': "lassen painting", 'file': "painting.jpg"},
        {'label': "black square", 'file': "black-square-16.png"},
        {'label': "red square", 'file': "red-square-16.png"},
        {'label': "green square", 'file': "green-square-16.png"},
        {'label': "blue square", 'file': "blue-square-16.png"},
        {'label': "white square", 'file': "white-square-16.png"},
        {'label': "blue square", 'file': "blue-square-16.jpg"},
        {'label': "blue square", 'file': "blue-square-16.gif"}
    ]
    # calculate attributes of image
    for color in color_dict:
        file = path + color['file']
        print(file)
        image_reference = Image.open(file)
        image_data = image_reference.getdata()
        color['format'] = image_reference.format
        color['mode'] = image_reference.mode
        color['size'] = image_reference.size
        color['array'] = np.array(image_data)
    return color_dict


@starter_bp.route('/binary/')
def binary():
    return render_template("starter/binary.html")


@starter_bp.route('/rgb', methods=["GET", "POST"])
def rgb():
    return render_template('starter/rgb.html', colors=color_data())


if __name__ == "__main__":
    colors = color_data("static/")  # path of local run
    for row in colors:
        # summarize some details about the image
        print(row['label'])
        print(row['format'])
        print(row['mode'])
        print(row['size'])
        print(row['array'])
        print()

        # open the image
        # image.show()
