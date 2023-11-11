import sys
def kadanes_algorithm(arr):
    maximum_sum = -sys.maxsize - 1
    current_sum = 0
    start = 0
    start_index, end_index = 0, 0
    for i in range(len(arr)):
        if current_sum == 0:
            start = i
        current_sum += arr[i]
        if current_sum > maximum_sum:
            start_index = start
            end_index = i
            maximum_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    if maximum_sum < 0:
        return 0
    for i in range(start_index, end_index+1):
        print(arr[i], end=" ")
    return maximum_sum

if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4] # 4 -1 2 1 = 6
    result = kadanes_algorithm(arr)
    print("Maximum subarray sum= ", result)