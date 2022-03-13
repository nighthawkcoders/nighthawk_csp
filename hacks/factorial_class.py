class Factorial:
    def fact(self, number):
        fact = 1
        for i in range(1, number + 1):
            fact = fact * i
        return fact


def tester():
    n = int(input("Enter a number for factorial: "))
    # make a factorial object
    obj = Factorial()
    result = obj.fact(n)
    print("Factorial of the given Number {0}! is:".format(n))
    print("{0}".format(result), end=" ")



if __name__ == "__main__":
    tester()
