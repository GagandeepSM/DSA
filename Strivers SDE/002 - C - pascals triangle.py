'''
Time complexity -> O(row) * O(row)
Space complexity -> O(1)
'''

def generate_row(row):
    element = 1
    ans = [element]
    for i in range(1, row):
        element = element * (row-i)
        element = element // i
        ans.append(element)
    
    return ans

def pascals_triangle(row):
    triangle = []
    for r in range(1, row + 1):
        current_row = generate_row(r)
        triangle.append(current_row)
    return triangle

if __name__ == '__main__':
    row = 6
    element = pascals_triangle(row)
    print(*element)