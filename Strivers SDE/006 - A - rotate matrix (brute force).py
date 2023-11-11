'''
    Rotate a matrix by 90 degree in clockwise direction brute force approach
    Time complexity: O(n^2)
    Space complexity: O(n^2)
'''

def rotateMatrix(matrix):
    n = len(matrix)
    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            result[j][n-i-1] = matrix[i][j]
    return result

if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    
    result = rotateMatrix(matrix)
    print(result)
