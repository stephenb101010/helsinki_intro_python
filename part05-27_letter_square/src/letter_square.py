import string

def fill_grid(grid : list, alphabets : list):
    alphabets_reversed = alphabets[::-1]
    north_row = 0
    south_row = len(grid)-1
    west_column = 0
    east_column = len(grid)-1

    for index, letter in enumerate(alphabets_reversed):
        if north_row == 0:
            for i in range(len(grid)):
                for j in range(len(grid)):
                    grid[i][j] = letter
        else:
            for r in range(north_row, south_row+1):
                for c in range(west_column, east_column+1):
                    grid[r][c] = letter
        north_row += 1
        south_row -= 1
        west_column += 1
        east_column -= 1
        if north_row == south_row:
            grid[north_row][south_row] = 'A'
            break

def print_grid(grid : list):
    formatted_grid = ''
    for row in grid:
        for letter in row:
            formatted_grid += letter
        formatted_grid += '\n'
    print(formatted_grid)

def square(alphabets : list):
    grid_size = (len(alphabets)*2)-1
    grid_row = []
    grid = []

    for i in range(grid_size):
        grid_row.append('#')

    for i in range(grid_size):
        grid.append(grid_row[:])

    fill_grid(grid, alphabets)
    print_grid(grid)

def main():
    layers = int(input('Layers: '))
    alphabets = list(string.ascii_uppercase)
    alphabets = alphabets[:layers]
    square(alphabets)

main()

'''
n = int(input("Layers: "))
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

left = ""    # section, that goes downwards
right = ""    # section, that goes upwards

k = n-1       # the location of next character in alphabets
m = 2*n-1     # the number of characters in between

while k >= 1:
    left = left+alphabets[k]
    right = alphabets[k]+right
    m -= 2
    print(left+alphabets[k]*m+right)
    k -= 1

while k <= n-1:
    print(left+alphabets[k]*m+right)
    left = left[:-1]
    right = right[1:]
    m += 2
    k += 1
'''