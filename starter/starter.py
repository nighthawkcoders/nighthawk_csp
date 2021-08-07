from flask import Blueprint, render_template
from PIL import Image
import numpy

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
    return render_template('starter/rgb.html', colors=color_data())


def color_data(path="starter/static/"):  # path of blueprint run is default
    # prefill with label and file
    color_dict = [
        {'source': "Peter Carolin", 'label': "Lassen Volcano", 'file': "lassen-volcano-256.jpg"},
        {'source': "iconsdb.com", 'label': "Black square", 'file': "black-square-16.png"},
        {'source': "iconsdb.com", 'label': "Red square", 'file': "red-square-16.png"},
        {'source': "iconsdb.com", 'label': "Green square", 'file': "green-square-16.png"},
        {'source': "iconsdb.com", 'label': "Blue square", 'file': "blue-square-16.png"},
        {'source': "iconsdb.com", 'label': "White square", 'file': "white-square-16.png"},
        {'source': "iconsdb.com", 'label': "Blue square", 'file': "blue-square-16.jpg"}
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
        color['data'] = numpy.array(image_data)
        color['hex_array'] = []
        color['binary_array'] = []
        for code in color['data']:
            hex_value = hex(code[0])[-2:] + hex(code[1])[-2:] + hex(code[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            color['hex_array'].append("#" + hex_value)
            bin_value = bin(int('1'+hex_value, 16))[3:]
            color['binary_array'].append("0b" + bin_value)
    return color_dict


if __name__ == "__main__":
    colors = color_data("static/")  # path of local run
    for row in colors:
        # summarize some details about the image
        print(row['label'])
        print(row['format'])
        print(row['mode'])
        print(row['size'])
        print(row['data'])
        print(row['hex_array'])
        print(row['binary_array'])
print()
