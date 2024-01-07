def grid(mat, i, j, n, m):
    if i >= n or j >= m:
        return 0
    if i == n-1 and j == m-1:
        return 1
    return grid(mat, i+1, j, n, m) + grid(mat, i, j+1, n, m)

mat = [[0, 0, 0], [0, 0, 0]]
n = len(mat)
m = len(mat[0])
print (grid(mat, 0, 0, n, m))