from flask import render_template
from __init__ import app

from y2021 import y2021_bp
from y2021.prep import y2021_prep_bp
from y2021.tri1 import y2021_tri1_bp
from y2021.tri2 import y2021_tri2_bp
from y2021.tri3 import y2021_tri3_bp
from algorithm.algorithm import algorithm_bp
from restapi.restapi import restapi_bp
from recipe.recipe import recipe_bp
from model.model import model_bp


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/deploy')
def deploy():
    return render_template("course/deploy.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


app.register_blueprint(y2021_bp)
app.register_blueprint(y2021_prep_bp)
app.register_blueprint(y2021_tri1_bp)
app.register_blueprint(y2021_tri2_bp)
app.register_blueprint(y2021_tri3_bp)
app.register_blueprint(restapi_bp)
app.register_blueprint(algorithm_bp)
app.register_blueprint(recipe_bp)
app.register_blueprint(model_bp)

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)
