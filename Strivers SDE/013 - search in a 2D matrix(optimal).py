'''
Search in a 2D matrix (Optimal)
Time complexity: O(log(m*n))
Space complexity: O(1)
'''

def searchMatrix(matrix, target):
    low = 0
    high = len(matrix[0]) * len(matrix) - 1
    while low <= high:
        mid = (low + high ) // 2   
        row = mid // len(matrix[0])
        col = mid % len(matrix[0])
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False  

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(searchMatrix(matrix, target)) # True