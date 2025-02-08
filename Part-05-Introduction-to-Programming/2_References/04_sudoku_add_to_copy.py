# Write your solution here
def print_sudoku(sudoku: list):
    a=0
    for row in sudoku:
        b=0
        for character in row:
            b += 1
            if character == 0:
                character = "_"
            string = f"{character} "
            if b % 3 == 0 and b < 8:
                string += " "
            print(string, end="")
        print()
        a +=1
        if a % 3 == 0 and a < 8:
            print()

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    
    #copy the matrix first
    sudoku_copy = [] #new matrix
    for x in range(len(sudoku)):
        new_row = [] #have to create a new row for each list inside matrix
        for y in range(len(sudoku)):
            new_row.append(sudoku[x][y])
        sudoku_copy.append(new_row)

    #main function
    sudoku_copy[row_no][column_no] = number
    return sudoku_copy


if __name__=="__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)