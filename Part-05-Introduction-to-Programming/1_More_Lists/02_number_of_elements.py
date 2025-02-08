# Write your solution here
def count_matching_elements(my_matrix: list, element: int):

    elements_sum = 0

    for row in my_matrix:
        for elements in row:
            if elements == element:
                elements_sum += 1
    
    return elements_sum

if __name__=="__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(count_matching_elements(m, 1))