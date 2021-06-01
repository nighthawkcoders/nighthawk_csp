# fundamental to API testing is request
import requests

# borrow these definitions from model
from model import print_tester, url_prefix


# play with api on localhost, server must be running
def api_tester():
    # local host URL for model
    url = 'http://127.0.0.1:5000/' + url_prefix

    # test conditions
    API = 0
    METHOD = 1
    tests = [
        ['/create/Wilma Flinstone/wilma@bedrock.org/123wifli/0001112222', "post"],
        ['/read/', "get"],
        ['/update/jmort1021@gmail.com/John C Mortensen', "put"],
        ['/delete/6', "delete"]
    ]

    # loop through each test condition and provide feedback
    for test in tests:
        print()
        print(f"({test[METHOD]}, {test[API]})")
        email = test[API].split("/")
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


if __name__ == "__main__":
    api_tester()  # validates api's requires server to be running
    print_tester()
