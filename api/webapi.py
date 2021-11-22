import random

from flask import Blueprint, jsonify

app_api = Blueprint('api', __name__,
                   url_prefix='/api',
                   template_folder='templates',
                   static_folder='static', static_url_path='static/api')

jokes_data = []
joke_list = [
    "If you give someone a program... you will frustrate them for a day; if you teach them how to program... you will "
    "frustrate them for a lifetime.",
    "Q: Why did I divide sin by tan? A: Just cos.",
    "UNIX is basically a simple operating system... but you have to be a genius to understand the simplicity.",
    "Enter any 11-digit prime number to continue.",
    "If at first you don't succeed; call it version 1.0.",
    "Java programmers are some of the most materialistic people I know, very object-oriented",
    "The oldest computer can be traced back to Adam and Eve. It was an apple but with extremely limited memory. Just "
    "1 byte. And then everything crashed.",
    "Q: Why did Wi-Fi and the computer get married? A: Because they had a connection",
    "Bill Gates teaches a kindergarten class to count to ten. 1, 2, 3, 3.1, 95, 98, ME, 2000, XP, Vista, 7, 8, 10.",
    "Q: What’s a aliens favorite computer key? A: the space bar!",
    "There are 10 types of people in the world: those who understand binary, and those who don’t.",
    "If it wasn't for C, we’d all be programming in BASI and OBOL.",
    "Computers make very fast, very accurate mistakes.",
    "Q: Why is it that programmers always confuse Halloween with Christmas? A: Because 31 OCT = 25 DEC.",
    "Q: How many programmers does it take to change a light bulb? A: None. It’s a hardware problem.",
    "The programmer got stuck in the shower because the instructions on the shampoo bottle said: Lather, Rinse, Repeat.",
    "Q: What is the biggest lie in the entire universe? A: I have read and agree to the Terms and Conditions.",
    'An SQL statement walks into a bar and sees two tables. It approaches, and asks may I join you?'
]


def _init_jokes():
    item_id = 1
    for item in joke_list:
        jokes_data.append({"id": item_id, "joke": item, "haha": 0, "boohoo": 0})
        item_id += 1


@app_api.route('/joke')
def joke():
    if len(jokes_data) == 0:
        _init_jokes()
    return jsonify(random.choice(jokes_data))


@app_api.route('/jokes')
def jokes():
    if len(jokes_data) == 0:
        _init_jokes()
    return jsonify(jokes_data)


if __name__ == "__main__":
    print(random.choice(joke_list))
