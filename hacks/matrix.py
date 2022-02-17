"""
Data Structures Introduction
Writing a function to print a Matrix
"""


# Classic nested loops using ij indexes
def print_matrix1(matrix):
    print("Classic nested loops using ij indexes")
    for i in range(len(matrix)):  # outer loop (i), built on length of matrix (rows)
        for j in range(len(matrix[i])):  # inner loop (j), built on length of items (columns)
            print(matrix[i][j], end=" ")  # [i][j] is 2D representation, end changes newline to space
        print()


# Enhanced nested for loops
def print_matrix2(matrix):
    print("Enhanced nested for loops")
    for row in matrix:  # short hand row iterator, index is not required
        for col in row:  # short hand column iterator
            print(col, end=" ")
        print()


# For loop with shortcut (*) row expansion (courtesy Raiden)
def print_matrix3(matrix):
    print("For loop with shortcut (*) row expansion")
    for row in matrix:
        print(*row)  # pythons has (*) that is one line expansion of row into columns


def test_matrices():
    # setup some text matrices
    keypad = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [" ", 0, " "]]

    keyboard = [["`", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, "-", "="],
                ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]"],
                ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'"],
                ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

    numbers = [[0, 1],
               [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
               [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]]

    # pack into a list of matrices with titles
    matrices = [["Keypad", keypad], ["Keyboard", keyboard], ["Number Systems", numbers]]

    # print each matrix using defined functions
    for title, matrix in matrices:  # unpack matrix with title
        print(title, len(matrix), "x", "~" + str(len(matrix[0])))  # formatted message with concatenation
        print_matrix1(matrix)
        print_matrix2(matrix)
        print_matrix3(matrix)
        print()


# tester section
if __name__ == "__main__":
    test_matrices()
