# Algorithm
## An algorithm typically means 'code' that solves a problem.  Designing an algorithm can take many forms.

### A Linear Sequence of code.  The order of executions is strictly from top to bottom.
#### The [lists.py](https://github.com/nighthawkcoders/nighthawk_csp/blob/master/algorithm/lists.py) is a sequence of code interacting with lists.

### A Procedure is a set of code instructions that has been abstracted into logical parts.  Each code abstraction is called "Procedural Abstraction", typically this means you are writing more "good" code vs "bad" code.  A procedure performs a defined set of instructions, typically receives input parameters, and returns an output result.  A procedure needs to be activated, or called!
#### The [image.py](https://github.com/nighthawkcoders/nighthawk_csp/blob/master/algorithm/image.py) has multiple procedures, Python "def" establishes a procedure, code that is indented inside the "def" is part of the procedures, These procedures are called by the 'main' tester at the bottom of the file.  Students should be familiar with this procedure from the work we did with the  Image Labs.  In the Image Labs a procedures was called/activated by Frontend actions, loading the menu.
#### The [bitwise.py](https://github.com/nighthawkcoders/nighthawk_csp/blob/master/algorithm/bitwise.py) has procedures associated with 'Truth Tables'.  This procedure was generated and shared with a few students working on the Logic Gates lab.  This file has a 'main' to enable testing as well The main activates and display results of logical operators, producing the 'Truth Table'.

### Variables combined with Procedures form the basis of Object-Oriented Programming.  Procedures are called after first creating a data object.  This is a philosophy of thinking about the end result and building variables and data to meeting that result all contained within a "Class" in Python.   In Python __init__ is where initial data is setup for the object.  Procedures (def) are called through the object.
#### The [fibonacci.py](https://github.com/nighthawkcoders/nighthawk_csp/blob/master/algorithm/fibonacci.py) follows OOP method.  This "Class" contains the series (nth sequence) and the algorithms to generate the nth sequence and all the steps that lead to that calculation.  THe class is constructed and procedures are called through the object, the 'main' at the bottom shows and runs the process.

#### Review of visual presentation of Fibonacci Algorithm
##### Number is taken as input: 10
##### Resulting fibonacci number is calculated: 34
##### Series is displayed in 'List' form: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
##### Build up series from 0 to 10 is shown
<img src="https://github.com/nighthawkcoders/nighthawk_csp/blob/master/algorithm/static/fibonacci.png" height="400" alt="">

#### The [palindrome.py](https://github.com/nighthawkcoders/nighthawk_csp/blob/master/algorithm/palindrome.py) follows OOP method as well.  This "Class" contains the candidate string and the algorithms determines if the string is a palindromes.   All the steps that lead to determining palindrome status are preserved in the object.  This does not contain a 'main'.

#### Review of visual presentation of Palindrome Algorithm
##### String is taken as input (word or phrase): "A man a plan a canal panama"
##### Algorithm takes 10 steps to determine result is "True", meaning string is a palindrome
##### Spaces, capitals, and some special characters are ignored in comparison
##### Each test from left most character to right most character are represented in 'testing series'
<img src="https://github.com/nighthawkcoders/nighthawk_csp/blob/master/algorithm/static/palindrome.png" height="400" alt="">
