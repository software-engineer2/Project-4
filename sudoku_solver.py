puzzle = [
    [7, 9, -1, -1, 3, -1, -1, 2, -1],
    [8, -1, 1, 4, -1, -1, -1, -1, 5],
    [-1, 3, -1, -1, 1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, 2, -1, 8],
    [-1, -1, -1, 7, -1, 9, -1, -1, -1],
    [1, -1, 8, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 6, -1, -1, 5, -1],
    [3, -1, -1, -1, -1, 4, 9, -1, 1],
    [-1, 8, -1, -1, 5, -1, -1, 3, 7],
]


def find_empty(sudoku):
    for row, element in enumerate(sudoku):
        for column, choice in enumerate(sudoku):
            if sudoku[row][column] == -1:
                return(row, column)

    return None, None


def valid(sudoku, number, r, c):
    a = False
    row = sudoku[r]
    if number in row:
        return a

    col = []
    for k, choice in enumerate(sudoku):
        col.append(sudoku[k][c])

    if number in col:
        return a

    row_split = r // 3 * 3
    column_split = c // 3 * 3

    for i in range(row_split, row_split + 3):
        for j in range(column_split, column_split + 3):
            if sudoku[i][j] == number:
                return a

    return not a


def find_solution(sudoku):
    a = False
    r, c = find_empty(sudoku)

    if r is None:
        return not a

    for number in range(1, 10):
        if valid(sudoku, number, r, c):
            sudoku[r][c] = number
            if find_solution(sudoku):
                return not a

        sudoku[r][c] = -1

    return a


def print_puzzle(puzzle):
    for l in range(len(puzzle)):
        if l % 3 == 0 and l != 0:
            print()

        for k in range(len(puzzle[0])):
            if k % 3 == 0 and k != 0:
                print(' ', end='')

            if k == 8:
                print(puzzle[l][k])
            else:
                print(str(puzzle[l][k]) + ' ', end='')


find_solution(puzzle)
print(print_puzzle(puzzle))
