# Math functions called from Menuy.py

# Python function to find Factors of a given number
def findFactors(number):
    print("Factors of a Given Number {0} are:".format(number))
    for value in range(1, number + 1):
        if number % value == 0:
            print("{0}".format(value), end=" ")


def factors():
    print("hello from factors")
    num = int(input("1.Please Enter any Number to find its factors: "))
    findFactors(num)


# Python function to find GCD of Two Numbers

def findgcd(num1, num2):
    if num1 == 0:
        return num1
        # print("\n GCD/HCF of {0} and {1} = {2}".format(a, b, b))

    while num2 != 0:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def gcd():
    a = int(input(" Please Enter the First Value for GCD: "))
    b = int(input(" Please Enter the Second Value for GCD: "))
    gcd = findgcd(a, b)
    print("\n GCD of {0} and {1} = {2}".format(a, b, gcd))
    print()


# Python function to find LCM of Two Numbers
def findlcm(a, b):
    if (a > b):
        maximum = a
    else:
        maximum = b
    while (True):
        if (maximum % a == 0 and maximum % b == 0):
            # print("\n Least Common Multiple of {0} and {1} = {2}".format(a, b, maximum))
            break;
        maximum = maximum + 1
    return maximum


def lcm():
    a = float(input(" Please Enter the First Value for LCM: "))
    b = float(input(" Please Enter the Second Value for LCM: "))
    lcm = findlcm(a, b)
    print("\n Least Common Multiple of {0} and {1} = {2}".format(a, b, lcm))

# Python function to find a range of primes 

def findprimes(min, max):
    for Number in range(min, max + 1):
        count = 0
        for i in range(2, (Number // 2 + 1)):
            if (Number % i == 0):
                count = count + 1
                break
        if (count == 0 and Number != 1):
            print(" %d" % Number, end='  ')
    print()


def primes():
    minimum = int(input(" Please Enter the Minimum Value for Primes: "))
    maximum = int(input(" Please Enter the Maximum Value for Primes: "))
    findprimes(minimum, maximum)
