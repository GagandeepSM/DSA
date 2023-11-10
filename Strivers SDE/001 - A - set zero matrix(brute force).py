'''
Brute Force Approach
Time complexity: O(M x N) x O(M + N) 
Space complexity: O(1)
'''

def mark_row(matrix, i, j, col):
    for j in range(0, col):
        if matrix[i][j]:
            matrix[i][j] = -1

def mark_col(matrix, i, j, row):
    for i in range(0, row):
        if matrix[i][j]:
            matrix[i][j] = -1

def set_zero_matrix(matrix, row, col):
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                mark_row(matrix, i, j, row, col)
                mark_col(matrix, i, j, row, col)

    for r in range(row):
        for c in range(col):
            if matrix[r][c] == -1:
                matrix[r][c] = 0 
    return matrix

if __name__ == "__main__":
    matrix = [[1, 1, 1], 
              [1, 0, 1], 
              [1, 1, 1]]
    row = len(matrix)
    col = len(matrix[0])
    result = set_zero_matrix(matrix, row, col)
    print(result) 

