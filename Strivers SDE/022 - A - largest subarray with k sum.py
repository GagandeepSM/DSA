def largest_subarray_with_k_sum(arr, n, k):
    largest_sum = 0
    for i in range(n):
        this_subarray_sum = 0
        for j in range(i, n):
            this_subarray_sum += arr[j]
            if this_subarray_sum == k:
                length_of_this_subarray = j - i + 1
                largest_sum = max(largest_sum, length_of_this_subarray)
    return largest_sum


if __name__ == '__main__':
    arr = [9, -3, 3, -1, 6, -5]
    n = len(arr)
    target_sum = 0
    print(largest_subarray_with_k_sum(arr, n, target_sum))