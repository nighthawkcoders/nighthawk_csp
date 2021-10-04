# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# JSON in Python: Python has a built-in package called json, which can be used to work with JSON data.
import json

# some dictionaries
dict_person = {"name": "Joe", "age": 61, "city": "San Diego"}
p1 = {"name": "John", "age": 61, "city": "Eugene"}
p2 = {"name": "Risa", "age": 16, "city": "New York"}
p3 = {"name": "Ryan", "age": 16, "city": "Los Angeles"}
p4 = {"name": "Shekar", "age": 16, "city": "San Francisco"}

print("Keys: ")
for key in dict_person:
    print(key)

print("Function Keys(): ")
for key in dict_person.keys():
    print(key)

print("Values: ")
for value in dict_person:
    print(dict_person[value])

print("Function Values(): ")
for value in dict_person.values():
    print(value)

print("Function Items(tuple): ")
for item in dict_person.items():
    print(item)

# a list of dictionaries
list_of_people = [p1, p2, p3, p4]
# write some code to Print List of people one by one
print("List of people")
print(type(list_of_people))
print(list_of_people)
print("Formatted list of people")
for person in list_of_people:
    print(person['name'] + "," + str(person['age']) + "," + person['city'])

# turn list to dictionary of people
dict_people = {'people': list_of_people}
print("List to Dictionary of people")
print(type(dict_people))
print(dict_people)
# write some code to Print People from Dictionary
# Using list comprehension
# Get values of a particular key in list of dictionaries
print("Name of People")
for person in dict_people['people']:
    print(person['name'])
# to list
names = [person['name'] for person in dict_people['people']]
print("Names of people to list: " + str(names))

# turn dictionary to JSON
print("** Dumps - Python to JSON String**")
json_people = json.dumps(list_of_people)
print("JSON People #1")
print(type(json_people))
print(json_people)
# write some code to print a space between each character of JSON
# hint use print(char, end ="-")
for i in range(len(json_people)):
    print(json_people[i], end=" ")
# pretty print JSON
json_print = json.dumps(list_of_people, indent=4, separators=("* ", " = "))
print(json_print)

# write some code to unwind JSON using json.loads and print the people
print("** Loads - JSON to Python Dict**")
json_dict = json.loads(json_people)
print(json_dict)
# to list
names = [person['name'] for person in json_dict]
print("Names of people to list: " + str(names))
print("Names of people: ")
# pretty print
for person in json_dict:
    print(person['name'])
