from PIL import Image, ImageDraw
import numpy


def color_data(path="static/img/", color_dict=None):  # path of blueprint run is default
    # prefill with label and file
    if color_dict is None:
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
        image_reference = Image.open(file)
        image_data = image_reference.getdata()
        color['path'] = '/' + path
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
            bin_value = bin(code[0])[2:].zfill(8) + " " + bin(code[1])[2:].zfill(8) + " " + bin(code[2])[2:].zfill(8)
            color['binary_array'].append(bin_value)
    return color_dict


if __name__ == "__main__":
    local_path = "../static/img/"
    color_test = [
        {'source': "Peter Carolin", 'label': "Lassen Volcano", 'file': "lassen-volcano-256.jpg"},
        {'source': "Peter Carolin", 'label': "Lassen Volcano", 'file': "lassen-volcano-original.jpg"},
    ]
    colors = color_data(local_path, color_test)  # path of local run
    for row in colors:
        # summarize some details about the image
        print(row['label'])
        print(row['format'])
        print(row['mode'])
        print(row['size'])
        print(row['data'])
        print(row['hex_array'])
        print(row['binary_array'])
        filename = local_path + row['file']
        image_ref = Image.open(filename)
        draw = ImageDraw.Draw(image_ref)
        draw.text((0, 0), "Size is {0} X {1}".format(*row['size']))
        image_ref.show()
print()
