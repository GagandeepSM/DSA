'''
Optimal approach:
Time complexity: O(M x N) + O(M x N)
Space complexity: O(1)
'''

def set_zero_matrix(matrix, row, col):
    col0 = 1
    for r in range(row):
        for c in range(col):
            if matrix[r][c] == 0:
                matrix [r][0] = 0
                if c != 0:
                    matrix [0][c] = 0
                else:
                    col0 = 0
    
    for r in range(1, row):
        for c in range(1, col):
            if matrix[r][c] != 0:
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
    
    if matrix[0][0] == 0:
        for c in range(col):
            matrix[0][c] = 0
    
    if col0 == 0:
        for r in range(row):
            matrix[r][0] = 0
    return matrix

if __name__ == '__main__':
    matrix = [[1, 1, 1],[1, 0, 1],[1, 1, 1]]
    row = len(matrix)
    col = len(matrix[0])
    result = set_zero_matrix(matrix, row, col)
    print(result)