# A Backtracking program
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


# Function to Find the entry
def findEmpty(grid, l):
    for row in range(6):
        for col in range(6):
            if (grid[row][col] == 0):
                l[0] = row
                l[1] = col
                return True
    return False


def usedRow(grid, row, num):
    for i in range(6):
        if (grid[row][i] == num):
            return True
    return False


def usedCol(grid, col, num):
    for i in range(6):
        if (grid[i][col] == num):
            return True
    return False



def isOk(grid, row, col, num):
    return not usedRow(grid, row, num) and \
           not usedCol(grid, col, num)


# Takes a partially filled-in grid
# and attempts to assign values to
# all unassigned locations
def solveSudoku(grid):
    # 'l' is a list variable that keeps the
    # record of row and col in
    # findEmpty Function
    l = [0, 0]

    if (not findEmpty(grid, l)):
        return True

    row = l[0]
    col = l[1]

    # consider digits 1 to 9
    for num in range(1, 7):

        # if looks promising
        if (isOk(grid, row, col, num)):

            # make tentative assignment
            grid[row][col] = num

            # return, if success,
            # ya !
            if (solveSudoku(grid)):
                return True

            # failure, unmake & try again
            grid[row][col] = 0

    # this triggers backtracking
    return False


# Driver main function to test above functions
def in_maker(grid):
    for i in range(N):
        for j in range(N):
            grid[i][j] = int(grid[i][j])
    return grid

def get_input(number):
    line_numbers = 6 * number
    for i in range(number):
        grid = []
        for line in range (N):
            line_input = input()
            grid.append(line_input.split(" "))
        grid = in_maker(grid)
        if (solveSudoku(grid)):
            adding(grid)
        else:
            print("no solution  exists ")

number = int(input())

get_input(number)
print("Method 2")
printing(number)