def longest_subsequence(arr, n):
    maximum = 0
    for i in range(n):
        element = arr[i]
        count = 1
        while element+1 in arr:
            element += 1
            count += 1
        maximum = max(count, maximum)
    return maximum

if __name__ == '__main__':
    arr = [1, 9, 3, 10, 4, 20, 2]
    n = len(arr)
    print(longest_subsequence(arr, n))
        


