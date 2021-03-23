from flask import Flask, render_template
from y2021 import y2021_bp
from y2021.prep import y2021_prep_bp
from y2021.tri1 import y2021_tri1_bp
from y2021.tri2 import y2021_tri2_bp
from y2021.tri3 import y2021_tri3_bp
from algorithm.app import algorithm_bp

app = Flask(__name__)
app.register_blueprint(y2021_bp, url_prefix='/y2021/repos')
app.register_blueprint(y2021_prep_bp, url_prefix='/y2021/prep')
app.register_blueprint(y2021_tri1_bp, url_prefix='/y2021/tri1')
app.register_blueprint(y2021_tri2_bp, url_prefix='/y2021/tri2')
app.register_blueprint(y2021_tri3_bp, url_prefix='/y2021/tri3')
app.register_blueprint(algorithm_bp, url_prefix='/algorithm')


@app.route('/')
def index():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5001")
