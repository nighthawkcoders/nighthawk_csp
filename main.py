from flask import render_template, request
from __init__ import app

from algorithm.algorithm import algorithm_bp
from crud.crud import model_bp
from recipe.recipe import recipe_bp
from restapi.restapi import restapi_bp
from starter.starter import starter_bp
from y2022 import y2022_bp


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/greet', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")


@app.route('/deploy')
def deploy():
    return render_template("course/deploy.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


app.register_blueprint(algorithm_bp)
app.register_blueprint(model_bp)
app.register_blueprint(recipe_bp)
app.register_blueprint(restapi_bp)
app.register_blueprint(starter_bp)
app.register_blueprint(y2022_bp)

if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5222")
