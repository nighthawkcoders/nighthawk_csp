"""
Data Structures Introduction
Writing a function to conditionally Swap data
"""


# define swap function with two parameters
def swap1(a, b):
    if a > b:
        b, a = a, b  # swap values
    return a, b  # return 2 values


# define order messaging function with two parameters
def swap1_helper(a, b):
    print("Python swap")
    print("Original: ", a, b)
    a, b = swap1(a, b)
    print("After: ", a, b)
    print()
    # no return value


def swap2(a, b):
    if a > b:
        swap = a  # classic swap technique
        a = b
        b = swap
    return a, b


def swap2_helper(a, b):
    print("Classic swap")
    print("Original: ", a, b)
    a, b = swap2(a, b)
    print("After: ", a, b)
    print()
    # no return value


def test_swappers():
    # call function order1
    swap1_helper(16, 10)  # send 2 parameters, expect swap
    swap1_helper(10, 16)  # no swap
    swap1_helper(10.1, 10)  # expect swap
    swap1_helper("def", "abc")  # expect swap
    swap1_helper("abc", "def")  # no swap
    swap1_helper("ddd", "dd")  # swap

    # call function order2
    swap2_helper(20, 16)
    swap2_helper(16, 20)
    swap2_helper(10.1, 10)
    swap2_helper("def", "abc")
    swap2_helper("abc", "def")
    swap2_helper("ddd", "dd")


if __name__ == "__main__":
    test_swappers()
