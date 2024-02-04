def count_subarray(arr, n, k):
    count = 0
    for i in range(n):
        temp_xor = arr[i]
        for j in range(i+1, n):
            if arr[j] ^ temp_xor == k:
                print(arr[i:j+1])
                count += 1
    return count

if __name__ == '__main__':
    arr = [4, 2, 2, 6, 4]
    n = len(arr)
    target_xor = 6
    print(count_subarray(arr, n, target_xor))