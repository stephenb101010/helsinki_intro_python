def print_sudoku(sudoku: list):
    for i in range(len(sudoku)):
        row_elements = ''
        for j in range(len(sudoku[i])):
            if sudoku[i][j] == 0:
                row_elements += '_ '
            else:
                row_elements += f'{sudoku[i][j]} '
            if (j+1)%3 == 0:
                row_elements += ' '
        print(row_elements)
        if (i+1)%3 == 0:
            print()

def add_number(sudoku: list, row_no: int, column_no: int, number:int):
    sudoku[row_no][column_no] = number

''' Model for print
def print_sudoku(sudoku: list):
    r = 0
    for row in sudoku:
        s = 0
        for character in row:
            s += 1
            if character == 0:
                character = "_"
            m = f"{character} "
            if s%3 == 0 and s < 8:
                m += " "
            print(m, end="")
        print()
        r += 1
        if r%3 == 0 and r < 8:
            print()
'''