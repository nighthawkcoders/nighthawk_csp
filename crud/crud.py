from flask import Blueprint, render_template, request, url_for, redirect

from crud.model import model_create, model_read, model_read_all, model_read_emails, \
    model_read_phones, model_update_name, model_delete
model_bp = Blueprint('crud', __name__,
                     url_prefix='/crud',
                     template_folder='templates',
                     static_folder='static',
                     static_url_path='assets')


# connects default URL to a function
@model_bp.route('/')
def crud():
    """convert Users table into a list of dictionary rows"""
    records = model_read_all()
    return render_template("crud/crud.html", table=records)


# create/add a new record to the table
@model_bp.route('/create/', methods=["POST"])
def create():
    if request.form:
        """extract data from form and call model_create"""
        model_create(
            request.form.get("name"),
            request.form.get("email"),
            request.form.get("password"),
            request.form.get("phone")
        )
    return redirect(url_for('model.crud'))


# CRUD read, which is filtering table based off of ID
@model_bp.route('/read/', methods=["POST"])
def read():
    record = []
    if request.form:
        userid = request.form.get("ID")
        # model_read expects userid
        user_dict = model_read(userid)
        # model_read returns: username, password, email, phone
        record = [user_dict]  # placed in list for compatibility with index.html
    return render_template("cryd/crud.html", table=record)


# CRUD update
@model_bp.route('/update/', methods=["POST"])
def update():
    if request.form:
        user_dict = {
            'userid': request.form.get("userid"),
            'name': request.form.get("name")
        }
        # model_update expects userid, email, phone
        model_update_name(user_dict)
    return redirect(url_for('model.crud'))


# CRUD delete
@model_bp.route('/delete/', methods=["POST"])
def delete():
    if request.form:
        """fetch userid"""
        userid = request.form.get("ID")
        model_delete(userid)
    return redirect(url_for('model.crud'))


# if email url, show the email table only
@model_bp.route('/emails/')
def emails():
    # fill the table with emails only
    records = model_read_emails()
    return render_template("crud/crud.html", table=records)


# if phones url, show phones table only
@model_bp.route('/phones/')
def phones():
    # fill the table with phone numbers only
    records = model_read_phones()
    return render_template("crud/crud.html", table=records)



