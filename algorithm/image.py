from PIL import Image, ImageDraw, ImageFilter
import numpy
import base64
from io import BytesIO
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f


# image (PNG, JPG) to base64 conversion (string), learn about base64 on wikipedia https://en.wikipedia.org/wiki/Base64
def image_base64(img, img_type):
    with BytesIO() as buffer:
        img.save(buffer, img_type)
        return base64.b64encode(buffer.getvalue()).decode()


# formatter preps base64 string for inclusion, ie <img src=[this return value] ... />
def image_formatter(img, img_type):
    return "data:image/" + img_type + ";base64," + image_base64(img, img_type)


# color_data prepares a series of images for data analysis
def image_data(path=Path("static/img/"), images=None):  # path of static images is defaulted
    if images is None:  # color_dict is defined with defaults
        images = [
            {'source': "Peter Carolin", 'label': "Lassen Volcano", 'file': "lassen-volcano-256.jpg"},
            {'source': "Peter Carolin", 'label': "Clouds Impression", 'file': "clouds-impression.png"}
        ]
    # gather analysis data and meta data for each image, adding attributes to each row in table
    for image in images:
        # File to open
        filename = path / image['file']  # file with path

        # Image open return PIL image object
        img_object = Image.open(filename)

        # Python Image Library operations
        image['format'] = img_object.format
        image['mode'] = img_object.mode
        image['size'] = img_object.size

        # Hacks here for images https://www.tutorialspoint.com/python_pillow/index.htm
        # use the open img_object!!!
        img_object = img_object.filter(ImageFilter.GaussianBlur)

        # Conversion of original Image to Base64, a string format that serves HTML nicely
        image['base64'] = image_formatter(img_object, image['format'])

        # Get data, use Numpy is used to access to data
        img_data = img_object.getdata()  # Reference https://www.geeksforgeeks.org/python-pil-image-getdata/
        image['data'] = numpy.array(img_data)
        image['hex_array'] = []
        image['binary_array'] = []
        image['gray_data'] = []

        # 'data' is a list of RGB data, the list is traversed and hex and binary lists are calculated and formatted
        for pixel in image['data']:
            # hexadecimal conversions
            hex_value = hex(pixel[0])[-2:] + hex(pixel[1])[-2:] + hex(pixel[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            image['hex_array'].append("#" + hex_value)
            # binary conversions
            bin_value = bin(pixel[0])[2:].zfill(8) + " " + bin(pixel[1])[2:].zfill(8) + " " + bin(pixel[2])[2:].zfill(8)
            image['binary_array'].append(bin_value)

            # create gray scale of image, ref: https://www.geeksforgeeks.org/convert-a-numpy-array-to-an-image/
            average = (pixel[0] + pixel[1] + pixel[2]) // 3  # integer division
            if len(pixel) > 3:
                image['gray_data'].append((average, average, average, pixel[3]))
            else:
                image['gray_data'].append((average, average, average))
        # end for loop for pixels

        # Conversion of modified Image to Base64
        img_object.putdata(image['gray_data'])
        image['base64_GRAY'] = image_formatter(img_object, image['format'])

    # end for loop for images
    return images  # list is returned with all the attributes for each image in a dictionary


# run this as standalone tester to see sample data printed in terminal
if __name__ == "__main__":
    local_path = Path("../starter/static/img/")
    images = image_data(local_path)  # path of local run
    for image in images:
        # print some details about the image so you can validate that it looks like it is working
        # meta data
        print("---- meta data -----")
        print(image['label'])
        print(image['format'])
        print(image['mode'])
        print(image['size'])
        # data
        print("----  data  -----")
        print(image['data'])
        print("----  gray data  -----")
        print(image['gray_data'])
        print("----  hex of data  -----")
        print(image['hex_array'])
        print("----  bin of data  -----")
        print(image['binary_array'])
        # base65
        print("----  base64  -----")
        print(image['base64'])

        # do so things to image that are not in image_info
        filename = local_path / image['file']
        img_object = Image.open(filename)

        # mess with the image
        img_object = img_object.transpose(Image.FLIP_TOP_BOTTOM)
        img_object = img_object.filter(ImageFilter.RankFilter)
        draw = ImageDraw.Draw(img_object)
        draw.text((0, 0), "Size is {0} X {1}".format(*image['size']))  # draw in image

        # open on desktop
        img_object.show()

    print()
