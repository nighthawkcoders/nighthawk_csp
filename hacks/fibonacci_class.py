# fibonacci_class.py

class Fibonacci:
    def __init__(self):
        self.fiboSeq = [0,1]

    #__call__ is a special function in Python that, when implemented inside a class,
    # gives its instances (objects) the ability to behave like a function.
    # It means after implementing __call__ method inside the Python class,
    # we can invoke its instances like a function
    def __call__(self, n):
        if n < len(self.fiboSeq):
            return self.fiboSeq[n]
        else:
            # Compute the requested Fibonacci number
            fib_number = self(n - 1) + self(n - 2)
            self.fiboSeq.append(fib_number)
        return self.fiboSeq[n]


def tester():
    # Make a fibonacci object
    while True:
        fibo_of = Fibonacci()
        n = input("Enter the number of terms: ")
        try:
            n = int(n)
            # Validate the value of n
            #The isinstance() function in Python returns true or false if a variable matches a
            # specified data type. isinstance(variable_to_check, data_type)
            if not (isinstance(n, int) and n >= 0):
                raise ValueError
            print("{0}th term  of Fibonacci sequence is: ".format(n))
            print(fibo_of(n-1)) # print the nth term
            print("Fibonacci sequence of {0} terms is: ".format(n))
            print([fibo_of(i) for i in range(0,n)])
            break
        except:
            print(f'Positive integer number expected, got "{n}" Try again.')

if __name__ == "__main__":
    tester()
