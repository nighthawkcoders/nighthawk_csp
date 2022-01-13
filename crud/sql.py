from __init__ import db
from crud.model import Users
# import random


# this is method called by frontend, it has been randomized between Alchemy and Native SQL for fun
def users_all():
    """  May have some problems with sql in deployment
    if random.randint(0, 1) == 0:
        table = users_all_alc()
    else:
        table = users_all_sql()
    return table
    """

    return users_all_alc()


# SQLAlchemy extract all users from database
def users_all_alc():
    table = Users.query.all()
    json_ready = [peep.read() for peep in table]
    return json_ready


# Native SQL extract all users from database
def users_all_sql():
    table = db.session.execute('select * from users')
    json_ready = sqlquery_2_list(table)
    return json_ready


# SQLAlchemy extract users from database matching term
def users_ilike(term):
    """filter Users table by term into JSON list (ordered by User.name)"""
    term = "%{}%".format(term)  # "ilike" is case insensitive and requires wrapped  %term%
    table = Users.query.order_by(Users.name).filter((Users.name.ilike(term)) | (Users.email.ilike(term)))
    return [peep.read() for peep in table]


# SQLAlchemy extract single user from database matching ID
def user_by_id(userid):
    """finds User in table matching userid """
    return Users.query.filter_by(userID=userid).first()


# SQLAlchemy extract single user from database matching email
def user_by_email(email):
    """finds User in table matching email """
    return Users.query.filter_by(email=email).first()


# ALGORITHM to convert the results of an SQL Query to a JSON ready format in Python
def sqlquery_2_list(rows):
    out_list = []
    keys = rows.keys()  # "Keys" are the columns of the sql query
    for values in rows:  # "Values" are rows within the SQL database
        row_dictionary = {}
        for i in range(len(keys)):  # This loop lines up K, V pairs, same as JSON style
            row_dictionary[keys[i]] = values[i]
        row_dictionary["query"] = "by_sql"  # This is for fun a little watermark
        out_list.append(row_dictionary)  # Finally we have a out_list row
    return out_list


# Test queries
if __name__ == "__main__":
    for i in range(10):
        print(users_all())
