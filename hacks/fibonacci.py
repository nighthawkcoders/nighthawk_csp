# Recursive function for Fibonacci series
def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

def driver():
    n = input("Enter number of terms for the fibonacci sequence: ")
    # validate #terms and run
    # execute selection
    # convert to number
    try:
        n = int(n)
        assert n > 0 # Test if it is positive
        print("Fibonacci sequence of {0} terms is: ".format(n))
        print([fibonacci_of(n) for n in range(n)])
    except AssertionError :
        print("Enter a positive number")
    except ValueError:
        # not a number error
        print(f"Not a number: {n}")

if __name__ == "__main__":
    driver()
