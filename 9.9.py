# N is the size of the 2D matrix   N*N
N = 6

SOLVED = []

def adding(grid):
    SOLVED.append(grid)
# print final sudoku
def printing(number):
    for k in range (number):
        print(k+1,") sudoku : ")
        for i in range(N):
            string = ""
            for j in range(N):
                if j != 5:
                    string = string + str(SOLVED[k][i][j]) + " "
                else:
                    string = string + str(SOLVED[k][i][j])
            print(string)



def isOk(grid, row, col, num):
    # Check if we find the same num in the similar row
    for x in range(N):
        if grid[row][x] == num:
            return False

    # Check if we find the same num in the similar col
    for x in range(N):
        if grid[x][col] == num:
            return False

    # Check if we find the same num in the 3*3 grid
    startRow = row - (row % 3)
    startCol = col - (col % 3)
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False

    # It's Ok!
    return True


def solveSudoku(grid, row, col):

    if (row == N - 1 and col == N):
        return True

    # Check if column value  becomes 9
    if col == N:
        row += 1
        col = 0

    # Check if the current position is filled
    if grid[row][col] > 0:
        return solveSudoku(grid, row, col + 1)

    for num in range(1, N + 1, 1):

        # Assign a number from 1 to 9 to a blank space
        if isOk(grid, row, col, num):
            grid[row][col] = num

            # Checking for next possibility
            if solveSudoku(grid, row, col + 1):
                return True

        # Removing the assigned num if it was wrong
        grid[row][col] = 0
    return False

def in_maker(grid):
    for i in range(N):
        for j in range(N):
            grid[i][j] = int(grid[i][j])
    return grid

def get_input(number):
    line_numbers = 9 * number
    for i in range(number):
        grid = []
        for line in range (N):
            line_input = input()
            grid.append(line_input.split(" "))
        grid = in_maker(grid)
        if (solveSudoku(grid, 0, 0)):
            adding(grid)
        else:
            print("no solution  exists ")

number = int(input())

get_input(number)
print("Method 1")
printing(number)



