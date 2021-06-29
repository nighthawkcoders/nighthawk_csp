class Palindrome:
    def __init__(self, candidate):
        self._candidate = candidate
        self._is_a_palindrome = False
        self._tests = 0
        self.is_palindrome()

    def is_palindrome(self):
        c = self._candidate.replace(" ", "")  # remove spaces
        # Run loop from 0 to len/2 of string (middle is exit point)
        tests = int(len(c) / 2)
        for i in range(0, tests):
            front = c[i];
            back = c[len(c) - i - 1]
            if front.lower() == back.lower():
                self._tests += 1
            else:
                return
        self._is_a_palindrome = True
        return

    @property
    def candidate(self):
        return self._candidate

    @property
    def tests(self):
        return self._tests

    @property
    def isPalindrome(self):
        return self._is_a_palindrome
