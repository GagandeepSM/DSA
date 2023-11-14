'''
    Rotate a matrix by 90 degree in clockwise direction optimal approach
    Time complexity: O(n^2)
    Space complexity: O(1)
'''

def rotateMatrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    
    result = rotateMatrix(matrix)
    print(result)
