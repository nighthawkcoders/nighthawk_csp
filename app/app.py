"""
Flask(__name__) establishes resources on the filesystem (aka package).
1. app is control object for flask
2. the Flask initializer uses __name__ param to locate root of webserver
3. static and templates are of folders that are located relative to directory of Flask execution
"""

from flask import Flask
from y2021.tri1.app import y2021_tri1_bp
from y2021.tri2.app import y2021_tri2_bp
from y2021.tri3.app import y2021_tri3_bp


app = Flask(__name__)
app.register_blueprint(y2021_tri1_bp, url_prefix='/y2021/tri1')
app.register_blueprint(y2021_tri2_bp, url_prefix='/y2021/tri2')
app.register_blueprint(y2021_tri3_bp, url_prefix='/y2021/tri3')


@app.route('/')
def index():
    return "Student Home Site"


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)
