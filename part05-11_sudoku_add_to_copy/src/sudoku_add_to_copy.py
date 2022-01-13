def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    copy = []
    for i in range(len(sudoku)):
        row = []
        for j in range(len(sudoku[i])):
            row.append(sudoku[i][j])
        copy.append(row)
    copy[row_no][column_no] = number
    return copy

''' Model:
def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
    new_list = []
    for r in sudoku:
        new_list.append(r[:])
                       ^^^^^^ - I messed up this part so I ended up with the above.
From the lesson: An easier way to copy a list is the bracket operator [], 
which we used for slices previously. The notation [:] selects all items in the collection. 
As a side effect, it creates a copy of the list.
    new_list[row_no][column_no] = number
    return new_list
'''

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