''' Dutch national flag problem
    Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
    Time Complexity: O(n)
    Space Complexity: O(1)
'''
def dutch_national_flag_problem(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid]  = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

if __name__ == '__main__':
    arr = [0, 2, 1, 2, 0]
    result = dutch_national_flag_problem(arr)
    print(result)