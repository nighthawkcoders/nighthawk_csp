from flask import Blueprint, render_template

app_y2022 = Blueprint('y2022', __name__,
                      url_prefix='/y2022',
                      template_folder='templates',
                      static_folder='static', static_url_path='/static/assets')


@app_y2022.route('/github')
def github():
    return render_template("course/github.html")

@app_y2022.route('/replit')
def replit():
    return render_template("course/replit.html")

@app_y2022.route('/deploy')
def deploy():
    return render_template("course/deploy.html")


@app_y2022.route('/tri1')
def tri1():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/csp2022tri1")


@app_y2022.route('/tri2')
def tri2():
    return render_template("course/timelines.html", padlet="https://padlet.com/jmortensen7/csp2022tri2")
