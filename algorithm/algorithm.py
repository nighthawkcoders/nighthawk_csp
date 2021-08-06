from flask import Blueprint, render_template, request
from .fibonacci import Fibonacci
from .palindrome import Palindrome

algorithm_bp = Blueprint('algorithm', __name__,
                         url_prefix='/algorithm',
                         template_folder='templates',
                         static_folder='static',
                         static_url_path='assets')

@algorithm_bp.route('/fibonacci/', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("algorithm/fibonacci.html", fibonacci=Fibonacci(int(request.form.get("series"))))
    return render_template("algorithm/fibonacci.html", fibonacci=Fibonacci(2))

@algorithm_bp.route('/palindrome/', methods=["GET", "POST"])
def palindrome():
    if request.form:
        return render_template("algorithm/palindrome.html", palindrome=Palindrome(request.form.get("candidate")))
    return render_template("algorithm/palindrome.html", palindrome=Palindrome("a toyota"))

