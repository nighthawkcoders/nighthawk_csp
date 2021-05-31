""" database setup to support db examples """
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
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone
        }

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

    class UpdateName(Resource):

        def put(self, name, email):
            person = Users.query.filter_by(email=email)
            person.update(dict(name=name))
            db.session.commit()

    class CreateUser(Resource):

        def post(self, name, email, password, phone):
            person = Users(name=name, email=email, password=password, phone=phone)
            db.session.add(person)
            db.session.commit()

            return person.json()

    class Read(Resource):
        def get(self):
            people = Users.query.all()

            return [peep.json() for peep in people]

    api.add_resource(Name, url_prefix+'/name/<string:name>')
    api.add_resource(CreateUser, url_prefix+'/create/<string:name>/<string:email>/<string:password>/<string:phone>')
    api.add_resource(Read, url_prefix+'/read')
    api.add_resource(UpdateName, url_prefix+'/update/<string:name>/<string:email>')



# CRUD create/add a new record to the table
# user_dict{} expects name, email, password, phone
def model_create(user_dict):
    """prepare data for primary table extracting from form"""
    if Users.query.filter_by(email=user_dict['email']).first() is None:
        user = Users(name=user_dict["name"],
                     email=user_dict["email"],
                     password=user_dict["password"],
                     phone=user_dict["phone"])
        """add and commit data to user table"""
        db.session.add(user)
        db.session.commit()


# CRUD read: filter single record in table based off of userid
# userid required
def model_read(userid):
    """filter users by userid"""
    user = Users.query.filter_by(userID=userid).first()
    user_dict = {'id': user.userID,
                 'name': user.name,
                 'email': user.email,
                 'password': user.password,
                 'phone': user.phone}
    return user_dict


# CRUD update
# user_dict{} expects userid, email, phone
def model_update(user_dict):
    """fetch userid"""
    userid = user_dict["userid"]
    if Users.query.filter_by(userID=userid).first() is not None:
        db.session.query(Users).filter_by(userID=userid).update(
            {Users.phone: user_dict['phone']})
    """commit changes to database"""
    db.session.commit()


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
    records = []
    users = Users.query.all()
    for user in users:
        user_dict = {'id': user.userID, 'name': user.name, 'email': user.email, 'password': user.password,
                     'phone': user.phone}
        records.append(user_dict)
    return records


# CRUD read: query emails table
def model_query_emails():
    # fill the table with emails only
    users = []
    records = Users.query.all()
    for record in records:
        user_dict = {'id': record.userID, 'email': record.email}
        users.append(user_dict)
    return users


# CRUD read: query phones table
def model_query_phones():
    # fill the table with phone numbers only
    users = []
    records = Users.query.all()
    for record in records:
        user_dict = {'id': record.userID, 'phone': record.phone}
        users.append(user_dict)
    return users


if __name__ == "__main__":
    """Tester data for table"""
    db.create_all()
    u1 = Users(name='Thomas Edison', email='tedison@example.com', password='toby', phone="1111111111")
    u2 = Users(name='Nicholas Tesla', email='ntesla@example.com', password='niko', phone="1111112222")
    u3 = Users(name='Alexander Graham Bell', email='agbell@example.com', password='lex', phone="1111113333")
    u4 = Users(name='Eli Whitney', email='eliw@example.com', password='whit', phone="1111114444")
    u5 = Users(name='John Mortensen', email='jmort1021@gmail.com', password='123qwerty', phone="8587754956")
    u6 = Users(name='John Mortensen', email='jmort1021@yahoo.com', password='123qwerty', phone="8587754956")
    u7 = Users(name='John Mortensen', email='jmort1021@yahoo.com', password='123qwerty', phone="8586791294")
    table = [u1, u2, u3, u4, u5, u6, u7]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {row.email}")

    print("Table: Users")
    result = model_query_all()
    for row in result:
        print(row)
