# define a function with two parameters
def order1(a, b):
    if a > b:
        b, a = a, b  # swap values
    return a, b  # 2 return values


def order2(a, b):
    if a > b:
        swap = a
        a = b
        b = swap
    return a, b


if __name__ == "__main__":
    print("Python swap")
    # call function order1, expect swap
    age1, age2 = order1(10, 16)     # call with parameters and return values
    print("Swap", age1, age2)
    # call function order1, no change
    age1, age2 = order1(16, 10)
    print("No Change", age1, age2)

    print()

    print("Classic swap")
    # call function order2, expect swap
    age1, age2 = order2(20, 16)
    print("Swap", age1, age2)
    # call function order2, no swap
    age1, age2 = order2(16, 20)
    print("No Change", age1, age2)