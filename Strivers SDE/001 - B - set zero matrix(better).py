'''
Better approach:
Time complexity: O(M x N) + O(M x N)
Space complexity: O(M) + O(N)
'''

def mark_row(matrix, row_array, row, col):
    for r in range(row):
        if row_array[r] == -1:
            for c in range(col):
                matrix[r][c] = 0    

def mark_col(matrix, col_array, row, col):
    for c in range(col):
        if col_array[c] == -1:
            for r in range(row):
                matrix[r][c] = 0

def set_zero_matrix(matrix, row, col):
    row_array = [0] * row 
    col_array = [0] * col
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 0:
                row_array[r] = -1
                col_array[c] = -1

    mark_row(matrix, row_array, row, col)
    mark_col(matrix, col_array, row, col)
    return matrix

if __name__ == '__main__':
    matrix = [[1, 1, 1],[1, 0, 1],[1, 1, 1]]
    row = len(matrix)
    col = len(matrix[0])
    result = set_zero_matrix(matrix, row, col)
    print(result)