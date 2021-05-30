from flask import Flask, render_template, request, url_for, redirect
from flask_login import LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from werkzeug.security import generate_password_hash, check_password_hash

from y2021 import y2021_bp
from y2021.prep import y2021_prep_bp
from y2021.tri1 import y2021_tri1_bp
from y2021.tri2 import y2021_tri2_bp
from y2021.tri3 import y2021_tri3_bp
from algorithm.app import algorithm_bp
from restapi.app import restapi_bp
from recipe.app import recipe_bp

app = Flask(__name__)
app.register_blueprint(y2021_bp)
app.register_blueprint(y2021_prep_bp)
app.register_blueprint(y2021_tri1_bp)
app.register_blueprint(y2021_tri2_bp)
app.register_blueprint(y2021_tri3_bp)
app.register_blueprint(restapi_bp)
app.register_blueprint(algorithm_bp)
app.register_blueprint(recipe_bp)

""" database setup to support db examples """
dbURI = 'sqlite:///model/myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)


# declare the users database model
class Users(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=True, nullable=False)


# Declare emails database model
class Emails(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    email_address = db.Column(db.String(255), unique=True, nullable=False)


# declare phone numbers database model
class PhoneNumbers(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    phone_number = db.Column(db.String(255), unique=True, nullable=False)


# declare authorised user account model
class AuthUser(UserMixin, db.Model):
    __tablename__ = 'authuser'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    website = db.Column(db.String(60), index=False, unique=False, nullable=True)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

    # must have set password method to create encrypted password
    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    # must have check password to check encrypted password
    def check_password(self, password):
        """Check hashed password."""
        result = check_password_hash(self.password, password)
        return result

    def __repr__(self):
        return '<AuthUser {}>'.format(self.name)


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


# connects default URL to a function
@app.route('/crud')
def crud():
    """convert Users table into a list of dictionary rows"""
    records = model_query_all()
    return render_template("crud.html", table=records)


# create/add a new record to the table
@app.route('/create/', methods=["POST"])
def create():
    if request.form:
        """extract data from form"""
        user_dict = {'username': request.form.get("username"), 'password': request.form.get("password"),
                     'email': request.form.get("email"), 'phone_number': request.form.get("phone_number")}
        # model_create expects: username, password, email, phone_number
        model_create(user_dict)
    return redirect(url_for('crud'))


# CRUD read, which is filtering table based off of ID
@app.route('/read/', methods=["POST"])
def read():
    record = []
    if request.form:
        userid = request.form.get("ID")
        # model_read expects userid
        user_dict = model_read(userid)
        # model_read returns: username, password, email, phone_number
        record = [user_dict]  # placed in list for compatibility with index.html
    return render_template("crud.html", table=record)


# CRUD update
@app.route('/update/', methods=["POST"])
def update():
    if request.form:
        user_dict = {
            'userid': request.form.get("ID"),
            'email': request.form.get("email"),
            'phone_number': request.form.get("phone_number")
        }
        # model_update expects userid, email, phone_number
        model_update(user_dict)
    return redirect(url_for('crud'))


# CRUD delete
@app.route('/delete/', methods=["POST"])
def delete():
    if request.form:
        """fetch userid"""
        userid = request.form.get("ID")
        model_delete(userid)
    return redirect(url_for('crud'))


# if email url, show the email table only
@app.route('/emails/')
def emails():
    # fill the table with emails only
    records = model_query_emails()
    return render_template("crud.html", table=records)


# if phones url, show phones table only
@app.route('/phones/')
def phones():
    # fill the table with phone numbers only
    records = model_query_phones()
    return render_template("crud.html", table=records)


# CRUD create/add a new record to the table
# user_dict{} expects username, password, email, phone_number
def model_create(user_dict):
    """prepare data for primary table extracting from form"""
    user = Users(username=user_dict["username"], password=user_dict["password"])
    """add and commit data to user table"""
    db.session.add(user)
    db.session.commit()
    """prepare data for related tables extracting from form and using new UserID """
    userid = db.session.query(func.max(Users.UserID))
    email = Emails(email_address=user_dict["email"], UserID=userid)
    phone_number = PhoneNumbers(phone_number=user_dict["phone_number"], UserID=userid)
    """email table add and commit"""
    db.session.add(email)
    db.session.commit()
    """phone number table add and commit"""
    db.session.add(phone_number)
    db.session.commit()


# CRUD read: filter single record in table based off of userid
# userid required
def model_read(userid):
    """filter users by userid"""
    user = Users.query.filter_by(UserID=userid).first()
    user_dict = {'id': user.UserID, 'name': user.username, 'password': user.password}
    """filter email by userid"""
    email = Emails.query.filter_by(UserID=userid).first()
    if email:
        user_dict['emails'] = email.email_address
    """filter phone number by userid"""
    pn = PhoneNumbers.query.filter_by(UserID=userid).first()
    if pn:
        user_dict['phone_numbers'] = pn.phone_number
    return user_dict


# CRUD update
# user_dict{} expects userid, email, phone_number
def model_update(user_dict):
    """fetch userid"""
    userid = user_dict["userid"]
    """update email in table from data in form if it exists, insert if not"""
    if Emails.query.filter_by(UserID=userid).first() is not None:
        db.session.query(Emails).filter_by(UserID=userid).update({Emails.email_address: user_dict["email"]})
    else:
        email = Emails(email_address=user_dict["email"], UserID=userid)
        db.session.add(email)
    """update phone number in table from data in form"""
    if PhoneNumbers.query.filter_by(UserID=userid).first() is not None:
        db.session.query(PhoneNumbers).filter_by(UserID=userid).update(
            {PhoneNumbers.phone_number: user_dict["phone_number"]})
    else:
        phone_number = PhoneNumbers(phone_number=user_dict["phone_number"], UserID=userid)
        db.session.add(phone_number)

    """commit changes to database"""
    db.session.commit()


# CRUD delete
# userid required
def model_delete(userid):
    """fetch userid"""
    userid = userid
    """delete userid rows from emails table"""
    db.session.query(Emails).filter(Emails.UserID == userid).delete()
    """delete userid rows from phone numbers table"""
    db.session.query(PhoneNumbers).filter(PhoneNumbers.UserID == userid).delete()
    """delete userid rows from users table"""
    db.session.query(Users).filter(Users.UserID == userid).delete()
    """commit changes to database"""
    db.session.commit()


# CRUD read: query all tables and records in the table
def model_query_all():
    """convert Users table into a list of dictionary rows"""
    records = []
    users = Users.query.all()
    for user in users:
        user_dict = {'id': user.UserID, 'name': user.username, 'password': user.password}
        # filter email
        email = Emails.query.filter_by(UserID=user.UserID).first()
        if email:
            user_dict['emails'] = email.email_address
        # filter phone number
        pn = PhoneNumbers.query.filter_by(UserID=user.UserID).first()
        if pn:
            user_dict['phone_numbers'] = pn.phone_number
        # append to records
        records.append(user_dict)
    return records


# CRUD read: query emails table
def model_query_emails():
    # fill the table with emails only
    records = []
    emails = Emails.query.all()
    for email in emails:
        user_dict = {'id': email.UserID, 'emails': email.email_address}
        records.append(user_dict)
    return records


# CRUD read: query phones table
def model_query_phones():
    # fill the table with phone numbers only
    records = []
    phone_numbers = PhoneNumbers.query.all()
    for phone in phone_numbers:
        user_dict = {'id': phone.UserID, 'phone_numbers': phone.phone_number}
        records.append(user_dict)
    return records


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True, port="5003")
