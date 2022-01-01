"""control dependencies to support CRUD app routes and APIs"""
from flask import Blueprint, render_template, request, url_for, redirect, jsonify, make_response
from flask_restful import Api, Resource
import requests
from crud.model import Users
from crud.app_crud import users_ilike, users_all, user_by_id, user_by_email
from crud.app_crud import app_crud

#Make sure you use APIs on your work, perhaps something is not returning JSON with Starus.

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects

app_crud_async = Blueprint('crud_async', __name__,
                            url_prefix='/crud_async',
                            template_folder='templates/crud/',
                            static_folder='static',
                            static_url_path='assets')

# API generator https://flask-restful.readthedocs.io/en/latest/api.html#id1
api = Api(app_crud_async)

""" Application control for CRUD is main focus of this File, key features:
    1.) User table queries
    2.) app routes (Bl  ueprint)
    3.) API routes
    4.) API testing
"""
""" Users table queries"""



""" app route section """
# Default URL
@app_crud_async.route('/')
def crud_async():
    """obtains all Users from table and loads Admin Form"""
    return render_template("crud_async.html", table=users_all())

""" API routes section """

class UsersAPI:

    # class for read/get
    class _ReadID(Resource):
        def get(self, userid):
            po = user_by_id(userid)
            if po is None:
                return {'message': f"{userid} is not found"}, 210
            data = po.read()
            response = make_response(jsonify(data), 200)
            return response

    # class for update/put
    class _UpdateName(Resource):
        def put(self, userid, name):
            po = user_by_id(userid)
            if po is not None:
                po.update(name)
            return po.read()



    # building RESTapi resource
    api.add_resource(_ReadID, '/read/<int:userid>')
    api.add_resource(_UpdateName, '/update/<int:userid>/<string:name>')


""" API testing section """
def api_tester():
    # local host URL for model
    url = 'http://localhost:5222/crud'
    # test conditions
    API = 0
    METHOD = 1
    tests = [
        ['/read/5', "get"],
        ['/update/1/Thomas Alva Edison', "put"]
    ]

    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {url + test[API]})")
        if test[METHOD] == 'get':
            response = requests.get(url + test[API])
        elif test[METHOD] == 'post':
            response = requests.post(url + test[API])
        elif test[METHOD] == 'put':
            response = requests.put(url + test[API])
        elif test[METHOD] == 'delete':
            response = requests.delete(url + test[API])
        else:
            print("unknown RESTapi method")
            continue

        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")

def api_printer():
    print()
    print("Users table")
    for user in users_all():
        print(user)

"""validating api's requires server to be running"""
if __name__ == "__main__":
    api_tester()
    api_printer()
