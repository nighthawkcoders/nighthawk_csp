from PIL import Image, ImageDraw
import numpy
import base64
from io import BytesIO


# image to base64 conversion, learn about base64 on wikipedia https://en.wikipedia.org/wiki/Base64
def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()


# formatter preps string format for <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)


# color_data prepares a series of images for data analysis
def image_data(path="static/img/", color_dict=None):  # path of static images is defaulted
    if color_dict is None:  # color_dict is defined with defaults
        color_dict = [
            {'source': "Peter Carolin", 'label': "Lassen Volcano", 'file': "lassen-volcano-256.jpg"},
            {'source': "iconsdb.com", 'label': "Black square", 'file': "black-square-16.png"},
            {'source': "iconsdb.com", 'label': "Red square", 'file': "red-square-16.png"},
            {'source': "iconsdb.com", 'label': "Green square", 'file': "green-square-16.png"},
            {'source': "iconsdb.com", 'label': "Blue square", 'file': "blue-square-16.png"},
            {'source': "iconsdb.com", 'label': "White square", 'file': "white-square-16.png"},
            {'source': "iconsdb.com", 'label': "Blue square", 'file': "blue-square-16.jpg"}
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for color in color_dict:
        color['path'] = '/' + path  # path for HTML access (frontend)
        file = path + color['file']  # file with path for local access (backend)
        # Python Image Library operations
        img_reference = Image.open(file)
        img_data = img_reference.getdata()
        color['format'] = img_reference.format
        color['mode'] = img_reference.mode
        color['size'] = img_reference.size
        # Conversion of original Image to Base64, a string format that serves HTML nicely
        color['base64'] = image_formatter(img_reference, color['format'])
        # Numpy is used to allow easy access to data of image, python list
        color['data'] = numpy.array(img_data)
        color['hex_array'] = []
        color['binary_array'] = []
        # Data list of RGB data traversed and hex and binary lists are created and formated
        for code in color['data']:
            # hexadecimal conversions
            hex_value = hex(code[0])[-2:] + hex(code[1])[-2:] + hex(code[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            color['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(code[0])[2:].zfill(8) + " " + bin(code[1])[2:].zfill(8) + " " + bin(code[2])[2:].zfill(8)
            color['binary_array'].append(bin_value)
    return color_dict  # dictionary is returned with all the attributes of these images


# run this as standalone tester to see data printed in terminal
if __name__ == "__main__":
    local_path = "../static/img/"
    color_test = [
        {'source': "iconsdb.com", 'label': "Red square", 'file': "red-square-16.png"},
    ]
    colors = image_data(local_path, color_test)  # path of local run
    for row in colors:
        # print some details about the image so you can validate that it looks like it is working
        print(row['label'])
        print(row['format'])
        print(row['mode'])
        print(row['size'])
        print(row['data'])
        print(row['hex_array'])
        print(row['binary_array'])
        print(row['base64'])
        filename = local_path + row['file']
        image_ref = Image.open(filename)
        draw = ImageDraw.Draw(image_ref)
        draw.text((0, 0), "Size is {0} X {1}".format(*row['size']))
        image_ref.show()
print()
