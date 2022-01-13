def row_correct(sudoku: list, row_no: int):
    row = sudoku[row_no]
    for element in row:
        if (element != 0) and row.count(element) != 1:
            return False
    return True

'''
    numbers = []
    for number in sudoku[row_no]:
        if number > 0 and number in numbers:
            return False
        numbers.append(number)
    return True
    '''