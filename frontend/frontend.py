from flask import Blueprint, render_template

app_frontend = Blueprint('frontend', __name__,
                         url_prefix='/frontend',
                         template_folder='templates/frontend/',
                         static_folder='static',
                         static_url_path='static/assets')


@app_frontend.route('/graph')
def graph():
    return render_template("graph.html")


@app_frontend.route('/life')
def life():
    return render_template("life.html")


@app_frontend.route('/snake')
def snake():
    return render_template("snake.html")
