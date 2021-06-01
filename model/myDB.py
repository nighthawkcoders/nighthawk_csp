""" database setup to support db examples """
import requests
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
from flask_restful import Resource, Api

from __init__ import app

dbURI = 'sqlite:///model/myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)

Migrate(app, db)
api = Api(app)
url_prefix = "/model"


# declare the users database model
class Users(db.Model):
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)

    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    def json(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone
        }

    class Create(Resource):
        def post(self, name, email, password, phone):
            person = model_create(name, email, password, phone)
            if person:
                return person.json()
            return {'email': None}, 404  # need to have better message on errors

    class Read(Resource):
        def get(self):
            return model_query_all()

    class UpdateName(Resource):
        def put(self, email, name):
            user = model_read_email(email)
            if user is None:
                return None
            model_update_name({'userid': user['userID'], 'name': name})
            return None  # needs error handling

    class UserID(Resource):
        def get(self, userid):
            person = Users.query.filter_by(userID=userid).first()
            if person:
                return person.json()
            return {'userID': None}, 404

        def delete(self, userid):
            person = Users.query.filter_by(userID=userid).first()
            db.session.delete(person)
            db.session.commit()

    class Name(Resource):
        def get(self, name):
            person = Users.query.filter_by(name=name).first()
            if person:
                return person.json()
            return {'name': None}, 404

        def delete(self, name):
            person = Users.query.filter_by(name=name).first()
            db.session.delete(person)
            db.session.commit()

    api.add_resource(Create, url_prefix + '/create/<string:name>/<string:email>/<string:password>/<string:phone>')
    api.add_resource(Read, url_prefix + '/read/')
    api.add_resource(UpdateName, url_prefix + '/update/<string:email>/<string:name>')
    api.add_resource(UserID, url_prefix + '/userid/<int:userid>')
    api.add_resource(Name, url_prefix + '/name/<string:name>')


# CRUD create/add a new record to the table
# user_dict{} expects name, email, password, phone
def model_create(name, email, password, phone):
    """prepare data for primary table extracting from form"""
    try:
        person = Users(
            name=name,
            email=email,
            password=password,
            phone=phone
        )
        db.session.add(person)
        db.session.commit()
        return person
    except:
        return None


# CRUD read: filter single record in table based off of userid
# userid required
def model_read(userid):
    """filter users by userid"""
    user = Users.query.filter_by(userID=userid).first()
    return user.json()


def model_read_email(email):
    """filter users by userid"""
    user = Users.query.filter_by(email=email).first()
    if user is None:
        return None
    return user.json()


# CRUD update
# model_update allows anything to be updated (excluding email)
def model_update_name(user_dict):
    """fetch userid"""
    userid = user_dict["userid"]
    user = Users.query.filter_by(userID=userid).first()
    if user is None:
        return None
    db.session.query(Users).filter_by(userID=userid).update({Users.name: user_dict['name']})
    """commit changes to database"""
    db.session.commit()
    return user.json


# CRUD delete
# userid required
def model_delete(userid):
    """fetch userid"""
    userid = userid
    db.session.query(Users).filter(Users.userID == userid).delete()
    """commit changes to database"""
    db.session.commit()


# CRUD read: query all tables and records in the table
def model_query_all():
    """convert Users table into a list of dictionary rows"""
    people = Users.query.all()
    return [peep.json() for peep in people]


# CRUD read: query emails
def model_query_emails():
    # fill the table with emails only
    people = Users.query.all()
    return [{'userID': peep.userID, 'email': peep.email} for peep in people]


# CRUD read: query phones
def model_query_phones():
    # fill the table with phone numbers only
    people = Users.query.all()
    return [{'userID': peep.userID, 'phone': peep.phone} for peep in people]


#### testing section
# create database from scratch
def model_tester():
    print("--------------------------")
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = Users(name='Thomas Edison', email='tedison@example.com', password='123toby', phone="1111111111")
    u2 = Users(name='Nicholas Tesla', email='ntesla@example.com', password='123niko', phone="1111112222")
    u3 = Users(name='Alexander Graham Bell', email='agbell@example.com', password='123lex', phone="1111113333")
    u4 = Users(name='Eli Whitney', email='eliw@example.com', password='123whit', phone="1111114444")
    u5 = Users(name='John Mortensen', email='jmort1021@gmail.com', password='123qwerty', phone="8587754956")
    u6 = Users(name='John Mortensen', email='jmort1021@yahoo.com', password='123qwerty', phone="8587754956")
    # U7 intended to fail as duplicate key
    u7 = Users(name='John Mortensen', email='jmort1021@yahoo.com', password='123qwerty', phone="8586791294")
    table = [u1, u2, u3, u4, u5, u6, u7]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {row.email}")
    record = model_read_email('jmort1021@yahoo.com')
    print()
    print("New Email Method", record['userID'], record['email'], record['name'])


# play with api
def api_tester():
    # local host URL for model
    url = 'http://127.0.0.1:5000/model'

    tests = [
        ['/read/', "get"],
        ['/userid/3', "get"],
        ['/name/John Mortensen', "get"],
        ['/create/Wilma Flinstone/wilma@bedrock.org/123wifli/0001112222', "post"],
        ['/update/jmort1021@yahoo.com/John C Mortensen', "put"],
        ['/name/John Mortensen', "get"],
        ['/name/John C Mortensen', "get"],
        ['/read/', "get"],
    ]
    # test conditions need to be incorporated in main api's
    API = 0
    METHOD = 1
    for test in tests:
        print()
        print(f"({test[METHOD]}, {test[API]})")
        email = test[API].split("/")
        if test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        else:
            response = requests.get(url + test[API])
        print(response)
        try:
            print(response.json())
        except:
            print("unhandled error")


# simple listing of table
def print_tester():
    print("------------")
    print("Table: users")
    print("------------")
    result = model_query_all()
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()  # builds model for user
    print_tester()
    api_tester()  # validates api's requires server to be running
    print_tester()
