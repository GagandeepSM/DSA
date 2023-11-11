'''
Time complexity -> O(row)
Space complexity -> O(1)
'''

def pascals_triangle(row):
    element = 1
    ans = [element]
    for i in range(1, row):
        element = element * (row-i)
        element = element // i
        ans.append(element)
    return ans

if __name__ == '__main__':
    row = 6
    element = pascals_triangle(row)
    print(*element)