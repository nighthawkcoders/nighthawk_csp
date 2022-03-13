# Recursive function for Fibonacci series
def fibonacci_of(n):
    if n in {0, 1}:  # Base case
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)  # Recursive case

def driver():
    n = int(input("Enter number of terms for the Fibonacci Sequence: "))
    print("Fibonacci sequence of {0} terms is: ".format(n))
    print([fibonacci_of(n) for n in range(15)])

if __name__ == "__main__":
    driver()
