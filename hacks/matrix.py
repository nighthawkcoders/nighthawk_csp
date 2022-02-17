# Classic nested loops using ij indexes
def print_matrix1(matrix):
    print("Classic nested loops using ij indexes")
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=" ")  # 2D representation
        print()


# Enhanced nested for loops
def print_matrix2(matrix):
    print("nested for loops")
    for row in matrix:
        for item in row:
            print(item, end=" ")
        print()


# For loop with shortcut (*) row expansion (courtesy Raiden)
def print_matrix3(matrix):
    print("for loop with * expansion")
    for row in matrix:
        print(*row)


# tester section
if __name__ == "__main__":
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print(len(matrix), "x 3")
    print_matrix1(matrix)
    print_matrix2(matrix)
    print_matrix3(matrix)

    print()
    matrix = [[0, 1, 2, 3],
              [4, 5, 6, 7],
              [8, 9, "A", "B"],
              ["C", "D", "E", "F"]]

    print(len(matrix), "x 4")
    print_matrix1(matrix)
    print_matrix2(matrix)
    print_matrix3(matrix)

    print()
    matrix = [[0, 1],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "A", "B", "C", "D", "E", "F"]]

    print(len(matrix), "x Mixed")
    print_matrix1(matrix)
    print_matrix2(matrix)
    print_matrix3(matrix)
