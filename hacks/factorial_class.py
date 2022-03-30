
class Factorial:
    def __init__(self):
        self.factorial = 1

        
'''

The call function/method is a special to Python, when implemented inside a class, this gives its
 object the ability to behave like a regular Python function.

Definition of call. The call method is defined inside the Python class. The method allows the 
construct object to invoke this method using a "object_name()" notation. The "def call(self, n):" 
has keyword "self" in the parameter list, this means that the object itself is part of this 
functions properties. The parameter "n" means it is expecting a value to be passed, 
in Factorial case it is for the Factorial of n - (n!).

'''        
    def __call__(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            # Compute the requested Fibonacci number
            self.factorial = n * self(n - 1)
        return self.factorial


def driver():
    # Make a fibonacci object
    fact_of = Factorial()
    n = input("Enter a number for factorial: ")
    try:
        n = int(n)
        # Validate the value of n
        if n < 0 or n > 99:
            raise ValueError

        print(f"Factorial  of {n}  is: ", fact_of(n))
    except ValueError:
        print(f'Positive integer number in range 2 to 99 is expected, got "{n}" Try again.')


if __name__ == "__main__":
    driver()
