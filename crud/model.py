""" database setup to support db examples """
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
from flask_restful import Resource, Api

from __init__ import app

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along

# Define variable to define type of database (sqlite), and name and location of myDB.db
dbURI = 'sqlite:///model/myDB.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)
api = Api(app)
# prefix for RESTful crud operations below, should change to api
url_prefix = "/crud"


# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class Users(db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, email, password, phone):
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone

    # return json/dictionary, self variables converter
    def json(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone
        }

    # class for create/post
    class Create(Resource):
        def post(self, name, email, password, phone):
            person = model_create(name, email, password, phone)
            if person:
                return person.json()
            return {'email': None}, 404  # need to have better message on errors

    # class for read/get
    class Read(Resource):
        def get(self):
            return model_read_all()

    # class for update/put
    class Update(Resource):
        def put(self, email, name):
            user = model_read_email(email)
            if user is None:
                return None
            model_update_name({'userid': user['userID'], 'name': name})
            return None  # needs error handling

    # class for delete
    class Delete(Resource):
        def delete(self, userid):
            model_delete(userid)

    # building RESTapi resource
    api.add_resource(Create, url_prefix + '/create/<string:name>/<string:email>/<string:password>/<string:phone>')
    api.add_resource(Read, url_prefix + '/read/')
    api.add_resource(Update, url_prefix + '/update/<string:email>/<string:name>')
    api.add_resource(Delete, url_prefix + '/delete/<int:userid>')


# CRUD create/add a new record to the table
# user_dict{} expects name, email, password, phone; returns person object on success
def model_create(name, email, password, phone):
    """prepare data for primary table extracting from form"""
    try:
        # creates a person object from Users(db.Model) class, passes initializers
        person = Users(
            name=name,
            email=email,
            password=password,
            phone=phone
        )
        db.session.add(person)  # add prepares to persist person object to Users table
        db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
        return person
    except IntegrityError:
        db.session.remove()
        return None


# CRUD read: filter single record in table based off of userid
# userid required, returns json/dictionary
def model_read(userid):
    """filter users by userid"""
    user = Users.query.filter_by(userID=userid).first()
    return user.json()


# CRUD read: filter single record in table based off of email
# userid required, returns json/dictionary
def model_read_email(email):
    """filter users by userid"""
    user = Users.query.filter_by(email=email).first()
    if user is None:
        return None
    return user.json()


# CRUD update: updates users name
# requires userid, returns json/dictionary
def model_update_name(user_dict):
    """fetch userid"""
    userid = user_dict["userid"]
    user = Users.query.filter_by(userID=userid).first()
    if user is None:
        return None
    db.session.query(Users).filter_by(userID=userid).update({Users.name: user_dict['name']})
    """commit changes to database"""
    db.session.commit()
    return user.json()


# CRUD delete: removes record from table
# userid required
def model_delete(userid):
    """fetch userid"""
    userid = userid
    db.session.query(Users).filter(Users.userID == userid).delete()
    """commit changes to database"""
    db.session.commit()


# CRUD read: query all tables and records in the table
def model_read_all():
    """convert Users table into a list of dictionary rows"""
    people = Users.query.all()
    return [peep.json() for peep in people]


# CRUD read: query by filter provided in term
def model_read_by_filter(term):
    # term structured in anywhere form
    term = "%{}%".format(term)
    # "ilike" is case insensitive partial match
    people = Users.query.filter((Users.name.ilike(term)) | (Users.email.ilike(term)))
    # return filtered Users table into a list of dictionary rows
    return [peep.json() for peep in people]


# CRUD read: query emails
def model_read_emails():
    # fill the table with emails only
    people = Users.query.all()
    return [{'userID': peep.userID, 'email': peep.email} for peep in people]


# CRUD read: query phones
def model_read_phones():
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


# simple listing of table
def print_tester():
    print("------------")
    print("Table: users with SQLAlchemy")
    print("------------")
    result = model_read_all()
    for row in result:
        print(row)

def print_tester2():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from users')
    print(result.keys())
    for row in result:
        print(row)

if __name__ == "__main__":
    model_tester()  # builds model of Users
    print_tester()
    print_tester2()



