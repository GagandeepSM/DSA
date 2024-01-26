import sys
def longest_subsequence(arr, n):
    arr.sort()
    count = 1
    maximum = 1
    for i in range(1, n):
        if arr[i] == arr[i-1] + 1:
            count += 1
        else:
            count = 1
        maximum = max(count, maximum)
    return maximum

if __name__ =='__main__':
    arr = [1, 9, 3, 10, 4, 20, 2]
    n = len(arr)
    print(longest_subsequence(arr, n))