# write your solution here
def form_matrix(): #convert the txt matrix to a list matrix
    main_matrix = []

    with open("matrix.txt") as matrix:
        for line in matrix:
            line = line.replace("\n","")
            newline = line.split(",")
            integers = []
            for number in newline:
                integers.append(int(number))
            main_matrix.append(integers)
    return main_matrix

def row_sums():
    matrix = form_matrix()
    sum_list = []
    
    for row in matrix:
        sum = 0
        for number in row:
            sum += number
        sum_list.append(sum)
    
    return sum_list

def matrix_sum():
    matrix_sum = sum(row_sums())
    return(matrix_sum)

def matrix_max():
    matrix = form_matrix()
    maximum = 0
    for line in matrix:
        for number in line:
            if number > maximum:
                maximum = number

    return maximum
