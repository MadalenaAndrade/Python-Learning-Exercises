# Write your solution here
def print_sudoku(sudoku:list):
    #create other list and 
    new_sudoku = []
    for row in sudoku:
        new_row = []
        for column in row:
            new_row.append(column)
        new_sudoku.append(new_row)

    #change 0 to _
    for i in range(len(new_sudoku)): 
        for j in range(len(new_sudoku)):
            if new_sudoku[i][j] == 0:
                new_sudoku[i][j] = "_" 
            else: #convert to string
                new_sudoku[i][j] = str(new_sudoku[i][j])
    

    #add spaces
    for line in new_sudoku:
        for index in range(len(line)-1):
            if index ==2 or index == 5:
                line[index] += "  "
            elif index < 8:
                line[index] += " "

     #print as grid string
    string = ""
    line_count = 0
    for line in new_sudoku:
        for column in line:
            string += column
        print(string) 
        string = ""
        line_count += 1
        if line_count == 3 or line_count == 6:
            print()
   
        
def add_number(sudoku: list, row_no: int, column_no: int, number: int):
    sudoku[row_no][column_no] = number
    


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

    print_sudoku(sudoku)  
    
    add_number(sudoku, 0, 0, 2)
    add_number(sudoku, 1, 2, 7)
    add_number(sudoku, 5, 7, 3)
    print()
    print("Three numbers added:")
    print()
    print_sudoku(sudoku)