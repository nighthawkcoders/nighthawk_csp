InfoDb = []
# List with dictionary key/values placed in a list
InfoDb.append({
    "FirstName": "John",
    "LastName": "Mortensen",
    "DOB": "October 21",
    "Residence": "San Diego",
    "Email": "jmortensen@powayusd.com",
    "Owns_Cars": ["2015-Fusion", "2011-Ranger", "2003-Excursion", "1997-F350", "1969-Cadillac"]
})

InfoDb.append({
    "FirstName": "Sunny",
    "LastName": "Naidu",
    "DOB": "August 2",
    "Residence": "San Diego",
    "Email": "snaidu@powayusd.com",
    "Owns_Cars": ["A", "B", "C"]
})


def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])    # using comma puts space between values
    print("\t", "Cars: ", end="")               # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Owns_Cars"]))    # join allows printing a string list with separator


def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)


def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return


def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return


if __name__ == "__main__":
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)
    print("Recursive loop")
    recursive_loop(0)
