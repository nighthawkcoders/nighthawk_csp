from flask import Blueprint, render_template, request
from .fibonacci import Fibonacci
from .palindrome import Palindrome

app_algorithm = Blueprint('algorithm', __name__,
                          url_prefix='/algorithm',
                          template_folder='templates/algorithm',
                          static_folder='static',
                          static_url_path='assets')


@app_algorithm.route('/fibonacci/', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("fibonacci.html", fibonacci=Fibonacci(int(request.form.get("series"))))
    return render_template("fibonacci.html", fibonacci=Fibonacci(2))


@app_algorithm.route('/palindrome/', methods=["GET", "POST"])
def palindrome():
    if request.form:
        return render_template("palindrome.html", palindrome=Palindrome(request.form.get("candidate")))
    return render_template("palindrome.html", palindrome=Palindrome("a toyota"))
