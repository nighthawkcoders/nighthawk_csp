
class Factorial:
    def __init__(self):
        self.factorial = 1

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
