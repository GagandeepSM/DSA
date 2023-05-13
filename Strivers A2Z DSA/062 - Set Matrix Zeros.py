'''
SET ZERO MATRIX

APPROACH 1: Brute Force
    TIME  : O(N*M) * O(N+M)
    SPACE : O(1)

APPROACH 2: USING DUMMY ARRAY
    TIME  : O(N*M) + O(N*M)
    SPACE : O(N) + O(M)

APPROACH 3: USING MATRIX's ROW AND COL OPTIMIZATION AND A COL-ZERO VARIABLE
    TIME  : O(N*M) + O(N*M)
    SPACE : O(1)
'''

def print_mat(mat):
    for i in mat:
        print(*i)
    print()

def approach1(mat):
    n_row = len(mat)
    n_col = len(mat[0])
    for r in range(n_row):
        for c in range(n_col):
            if mat[r][c] == 0:                
                for i in range(0,r):
                    mat[i][c] = -1
                for i in range(r+1,n_row):
                    mat[i][c] = -1
                for j in range(0,c):
                    mat[r][j] = -1
                for j in range(c+1,n_col):
                    mat[r][j] = -1
                    
    for r in range(n_row):
        for c in range(n_col):
            if mat[r][c] == -1:
                mat[r][c] = 0     
    return mat

def approach2(mat):
    n_row = len(mat)
    n_col = len(mat[0])
    dummy_row = [0]*n_row
    dummy_col = [0]*n_col
    
    for r in range(n_row):
        for c in range(n_col):
            if mat[r][c] == 0:
                dummy_row[r] = 1
                dummy_col[c] = 1
                
    for r in range(n_row):
        for c in range(n_col):
            if dummy_row[r] or dummy_col[c]:
                mat[r][c] = 0
    return mat

def approach3(mat):
    col0 = 1
    n_row = len(mat)
    n_col = len(mat[0])

    for r in range(n_row):
        for c in range(n_col):
            if mat[r][c] == 0:
                mat[r][0] = 0
                if c:
                    mat[0][c] = 0
                else:
                    col0 = 0
        
    for r in range(1,n_row):
        for c in range(1,n_col):
            if mat[0][c] == 0 or mat[r][0] == 0 :
                mat[r][c] = 0

    if mat[0][0] == 0:
        for i in range(n_col):
            mat[0][i] = 0
    if col0==0:
        for i in range(n_col):
            mat[i][0] = 0

    return mat
    
if __name__ == '__main__':
    matrix1 = [
        [1,1,1,1,1],
        [1,0,0,1,1],
        [1,1,0,1,1],
        [1,1,1,1,1],
        ]
    
    result1 = approach1(matrix1)
    print_mat(result1)

    matrix2 = [
        [1,1,1,1],
        [1,0,1,1],
        [1,1,0,1],
        [0,1,1,1],
        ]
    result2 = approach2(matrix2)
    print_mat(result2)
    
    matrix3 = [
        [1,1,1,1,1],
        [1,0,0,1,1],
        [1,1,0,1,1],
        [1,1,1,1,1],
        ]
    
    result3 = approach3(matrix3)
    print_mat(result3)    
