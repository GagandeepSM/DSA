def longest_subsequence(arr, n):
    my_set = set(arr)
    largest = 1
    for item in arr:
        if (item - 1) not in my_set:
            count = 1
            while item + 1 in my_set: 
                count += 1
                item = item+1
            largest = max(largest, count)
    return largest

if __name__ =='__main__':
    arr = [1, 9, 3, 10, 4, 20, 2]
    n = len(arr)
    print(longest_subsequence(arr, n))