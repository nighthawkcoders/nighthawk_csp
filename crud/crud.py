# flask imports
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
# model imports
from .model import model_create, model_read, model_read_all, model_read_emails, \
    model_read_phones, model_update_name, model_delete, model_read_by_filter

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
        model_create(
            request.form.get("name"),
            request.form.get("email"),
            request.form.get("password"),
            request.form.get("phone")
        )
    return redirect(url_for('.crud'))


# CRUD read, which is filtering table based off of ID
@app_crud.route('/read/', methods=["POST"])
def read():
    record = []
    if request.form:
        userid = request.form.get("ID")
        # model_read expects userid and returns a dictionary of user data: username, password, email, phone
        user_dict = model_read(userid)
        record = [user_dict]  # placed in list for easy use within HTML
    return render_template("crud.html", table=record)


# CRUD update
@app_crud.route('/update/', methods=["POST"])
def update():
    if request.form:
        user_dict = {
            'userid': request.form.get("userid"),
            'name': request.form.get("name")
        }
        # model_update expects userid and name in a dictionary
        model_update_name(user_dict)
    return redirect(url_for('.crud'))


# CRUD delete
@app_crud.route('/delete/', methods=["POST"])
def delete():
    if request.form:
        """fetch userid"""
        userid = request.form.get("ID")
        # model_delete expects a userid
        model_delete(userid)
    return redirect(url_for('.crud'))


# if email url, show the email table only
@app_crud.route('/emails/')
def emails():
    # fill the table with emails only
    records = model_read_emails()
    return render_template("crud.html", table=records)


# if phones url, show phones table only
@app_crud.route('/phones/')
def phones():
    # fill the table with phone numbers only
    records = model_read_phones()
    return render_template("crud.html", table=records)


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
