'''
To print an element present at a given position (r, c) in pascal's triangle:
Time complexity: O(c) # c is the column number
'''
def nCr(n, r):
    res = 1
    for i in range(r):
        res = res * (n - i)
        res = res // (i + 1) 
    
def pascals_triangle(row, col):
    res = nCr(row - 1, col - 1)
    return res

if __name__ == '__main__':
    row = 5  
    col = 3  
    element = pascals_triangle(row, col)
    print(f"The element at position (r, c) is: {element}")