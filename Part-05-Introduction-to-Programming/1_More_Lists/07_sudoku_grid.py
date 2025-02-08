# Write your solution here
def row_correct(sudoku: list, row_no: int): #check row

    #taking out the zeros
    filled_numbers = []

    for element in sudoku[row_no]:
        if element != 0:
            filled_numbers.append(element) 

    #checking repeated numbers
    repeatednumbers = []
    for number in filled_numbers:
        if number in repeatednumbers:
            return False
        repeatednumbers.append(number)
    return True

#check column
def column_correct(sudoku:list, column_no:int):

    checked_column = []
    for row in sudoku:
        checked_column.append(row[column_no])

    used_numbers = []
    for number in checked_column:
        if number > 0 and number in used_numbers:
            return False
        used_numbers.append(number)
    
    return True

#check block
def block_correct(sudoku:list, row_no:int, column_no:int):
    
    #create block
    block = []
    for x in range(3):
        for y in range(3):
            block.append(sudoku[row_no+x][column_no+y])

    #check for repetition
    numbers_list = []
    for number in block:
        if number >0 and number in numbers_list:
            return False
        numbers_list.append(number)
    return True

#all together
def sudoku_grid_correct(sudoku: list):
        for row in range(len(sudoku)):
            if not row_correct(sudoku, row):
                return False
        
        for column in range(len(sudoku)):
            if not column_correct(sudoku, column):
                return False
        
        x=0
        y=0
        while x < 7:
            while y < 7:
                if not block_correct(sudoku, x, y):
                    return False
                y += 3
            y = 0
            x += 3
        return True
            

if __name__=="__main__":
    sudoku1 = [
  [ 2, 9, 5, 0, 8, 4, 7, 1, 3 ],
  [ 6, 4, 8, 1, 3, 7, 9, 2, 5 ],
  [ 1, 7, 3, 2, 0, 9, 4, 6, 8 ],
  [ 8, 6, 0, 3, 4, 1, 2, 5, 7 ],
  [ 5, 2, 7, 8, 9, 6, 0, 3, 4 ],
  [ 3, 1, 4, 0, 7, 2, 6, 8, 9 ],
  [ 7, 5, 0, 9, 2, 8, 1, 4, 0 ],
  [ 4, 3, 6, 7, 1, 5, 8, 0, 2 ],
  [ 0, 8, 0, 4, 6, 3, 5, 7, 1 ],    
    ]
    print(sudoku_grid_correct(sudoku1)) 
