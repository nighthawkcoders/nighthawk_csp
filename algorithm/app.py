from flask import Blueprint, render_template, request
from algorithm.fibonacci import Fibonacci

algorithm_bp = Blueprint('algorithm', __name__,
                         template_folder='templates',
                         static_folder='static', static_url_path='assets')


@algorithm_bp.route('/fibonacci', methods=["GET", "POST"])
def fibonacci():
    if request.form:
        return render_template("algorithm/fibonacci.html", fibonacci=Fibonacci(int(request.form.get("series"))))
    return render_template("algorithm/fibonacci.html", fibonacci=Fibonacci(2))
