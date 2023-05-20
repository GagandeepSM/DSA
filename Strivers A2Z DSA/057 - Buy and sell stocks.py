'''
BUY AND SELL STOCKS

APPROACH 1: BRUTE FORCE
    T(C) : O(N^2)
    S(C) : O(1)

APPROACH 2: STORAGE 
    T(C) : O(N)
    S(C) : O(1)
    
'''

def approach2(arr, n):
    mini = 100000000
    maxi = -1
    profit = -1
    for i in range(n):
        print(arr[i], mini,maxi, profit)
        if arr[i] < mini:
            mini = arr[i]
            maxi = arr[i]
            
        if arr[i] > maxi:
            maxi = arr[i]
            if profit < maxi - mini:
                profit = maxi-mini
    return profit
            
            
n = 6
arr = [7000,1,5,900,6,80]

res = approach2(arr, n)
print(res)
