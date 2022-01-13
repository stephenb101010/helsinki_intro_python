def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    for element in row:
        if element != 0 and row.count(element) != 1:
            return False
    return True
    
def column_correct(sudoku: list, column_no: int):
    column = []
    for row in sudoku:
        column.append(row[column_no])
    for element in column:
        if (element != 0) and (column.count(element) != 1):
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    block = []
    for i in range(row_no, row_no + 3):
        for j in range(column_no, column_no + 3):
            block.append(sudoku[i][j])
    
    for element in block:
        if (element != 0) and (block.count(element) != 1):
            return False
    return True

def sudoku_grid_correct(sudoku: list):
    blocks = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]

    for i in range(9):
        if row_correct(sudoku, i) == False or column_correct(sudoku, i) == False or block_correct(sudoku, blocks[i][0], blocks[i][1]) == False:
            return False
    return True

''' MOdel solution
def row_correct(sudoku: list, row_no: int):
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
    return True

def column_correct(sudoku: list, column_no: int):
    numbers = []
    for row in sudoku:
        number = row[column_no]
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    numbers = []
    for r in range(row_no, row_no+3):
        for s in range(column_no, column_no+3):
            number = sudoku[r][s]
            if number > 0 and number in numbers:
                return False
            numbers.append(number)
    return True

def sudoku_grid_correct(sudoku: list):
    for row in range(0,9):
        if not row_correct(sudoku, row):
            return False

    for column in range(0,9):
        if not column_correct(sudoku, column):
            return False

    for row in range(0,9,3):
        for column in range(0,9,3):
            if not block_correct(sudoku, row, column):
                return False
    return True
'''