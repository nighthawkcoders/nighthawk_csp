""" database setup to support db examples """
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

from __init__ import app

dbURI = 'sqlite:///model/myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
db = SQLAlchemy(app)


# declare the users database model
class Users(db.Model):
    UserID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    phone = db.Column(db.String(255), unique=False, nullable=False)


# CRUD create/add a new record to the table
# user_dict{} expects name, email, password, phone
def model_create(user_dict):
    """prepare data for primary table extracting from form"""
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
    user = Users.query.filter_by(UserID=userid).first()
    user_dict = {'id': user.UserID,
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
    if Users.query.filter_by(UserID=userid).first() is not None:
        db.session.query(Users).filter_by(UserID=userid).update(
            {Users.phone: user_dict['phone']})
    """commit changes to database"""
    db.session.commit()


# CRUD delete
# userid required
def model_delete(userid):
    """fetch userid"""
    userid = userid
    db.session.query(Users).filter(Users.UserID == userid).delete()
    """commit changes to database"""
    db.session.commit()


# CRUD read: query all tables and records in the table
def model_query_all():
    """convert Users table into a list of dictionary rows"""
    records = []
    users = Users.query.all()
    for user in users:
        user_dict = {'id': user.UserID, 'name': user.name, 'email': user.email, 'password': user.password,
                     'phone': user.phone}
        records.append(user_dict)
    return records


# CRUD read: query emails table
def model_query_emails():
    # fill the table with emails only
    users = []
    records = Users.query.all()
    for record in records:
        user_dict = {'id': record.UserID, 'email': record.email}
        users.append(user_dict)
    return users


# CRUD read: query phones table
def model_query_phones():
    # fill the table with phone numbers only
    users = []
    records = Users.query.all()
    for record in records:
        user_dict = {'id': record.UserID, 'phone': record.phone}
        users.append(user_dict)
    return users


if __name__ == "__main__":
    """Tester data for table"""
    db.create_all()
    u1 = Users(name='Thomas Edison', email='tedison@example.com', password='toby', phone="111-111-1111")
    u2 = Users(name='Nicholas Tesla', email='ntesla@example.com', password='niko', phone="111-111-2222")
    u3 = Users(name='Alexander Graham Bell', email='agbell@example.com', password='lex', phone="111-111-3333")
    u4 = Users(name='Eli Whitney', email='eliw@example.com', password='whit', phone="111-111-4444")
    u5 = Users(name='John Mortensen', email='jmort1021@gmail.com', password='123qwerty', phone="858-775-4956")
    u6 = Users(name='John Mortensen', email='jmort1021@yahoo.com', password='123qwerty', phone="858-775-4956")
    u7 = Users(name='John Mortensen', email='jmort1021@yahoo.com', password='123qwerty', phone="858-679-1294")
    table = [u1, u2, u3, u4, u5, u6, u7]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist or duplicate email: {row.email}")

    print("Table: Users")
    result = model_query_all()
    for row in result:
        print(row)
