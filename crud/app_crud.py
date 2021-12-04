# flask imports
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
# model imports
from crud.model import Users, model_read_all, model_read_by_filter

# blueprint defaults
app_crud = Blueprint('crud', __name__,
                     url_prefix='/crud',
                     template_folder='templates/crud/',
                     static_folder='static',
                     static_url_path='assets')


# ##### Routes within this blueprint broker information between HTML and Model code
# Default URL of blueprint and connecting to crud() function
@app_crud.route('/')
def crud():
    """extracts Users table from DB and returns in json format"""
    records = model_read_all()
    return render_template("crud.html", table=records)


# CRUD create/add a new record to the table
@app_crud.route('/create/', methods=["POST"])
def create():
    if request.form:
        """extract data from form and call model_create"""
        po = Users(
            request.form.get("name"),
            request.form.get("email"),
            request.form.get("password"),
            request.form.get("phone")
        )
        po.create()
    return redirect(url_for('.crud'))


# CRUD read, which is filtering table based off of ID
@app_crud.route('/read/', methods=["POST"])
def read():
    table = []
    if request.form:
        userid = request.form.get("userid")
        po = Users.query.filter_by(userID=userid).first()
        if po is not None:
            table = [po.read()]  # placed in list for easier/consistent use within HTML
    return render_template("crud.html", table=table)


# CRUD update
@app_crud.route('/update/', methods=["POST"])
def update():
    if request.form:
        userid =  request.form.get("userid")
        name = request.form.get("name")
        po = Users.query.filter_by(userID=userid).first()
        if po is not None:
            po.update(name)
    return redirect(url_for('crud.crud'))


# CRUD delete
@app_crud.route('/delete/', methods=["POST"])
def delete():
    if request.form:
        userid = request.form.get("userid")
        po = Users.query.filter_by(userID=userid).first()
        if po is not None:
            po.delete()
    return redirect(url_for('crud.crud'))


@app_crud.route('/search/')
def search():
    return render_template("search.html")


@app_crud.route('/search/term/', methods=["POST"])
def search_term():
    req = request.get_json()
    term = req['term']
    query = model_read_by_filter(term)
    response = make_response(jsonify(query), 200)

    return response
