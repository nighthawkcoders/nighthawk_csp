from flask import Flask, render_template
from y2021.tri1 import y2021_tri1_bp
from y2021.tri2 import y2021_tri2_bp
from y2021.tri3 import y2021_tri3_bp

app = Flask(__name__)
app.register_blueprint(y2021_tri1_bp, url_prefix='/y2021/tri1')
app.register_blueprint(y2021_tri1_bp, url_prefix='/y2021/tri1')
app.register_blueprint(y2021_tri2_bp, url_prefix='/y2021/tri2')
app.register_blueprint(y2021_tri3_bp, url_prefix='/y2021/tri3')


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5001")
