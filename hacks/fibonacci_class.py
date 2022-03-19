# fibonacci_class.py

class Fibonacci:
    def __init__(self):
        self.fiboseq = [0, 1]

    #__call__ is a special function in Python that, when implemented inside a class,
    # gives its instances (objects) the ability to behave like a function.
    # It means after implementing __call__ method inside the Python class,
    # we can invoke its instances like a function
    def __call__(self, n):
        # Validate the value of n
        #The isinstance() function in Python returns true or false if a variable matches a
        # specified data type. isinstance(variable_to_check, data_type)
        if not (isinstance(n, int) and n >= 0):
                raise ValueError
        if n < len(self.fiboseq):
            return self.fiboseq[n]
        else:
            # Compute and cache the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.fiboseq.append(fib_number)
            return self.fiboseq[n]


def tester():
    #make a fibonacci object
    fibo_of = Fibonacci()
    n = input("Enter the number of terms: ")
    try:
        n = int(n)
        if not (isinstance(n, int) and n >= 0):
            raise ValueError
        print("Fibonacci sequence of {0} terms is: ".format(n))
        print([fibo_of(i) for i in range(0,n)]) # print n # of terms
    except:
        print(f'Positive integer number expected, got "{n}"')

if __name__ == "__main__":
    tester()
