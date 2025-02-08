# Write your solution here
def transpose(matrix:list):
    used_i = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j and j not in used_i:
                used_i.append(i)
                new_i = matrix[j][i]
                new_j = matrix[i][j]
                matrix[i][j] = new_i
                matrix[j][i] = new_j


if __name__=="__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(transpose(matrix))