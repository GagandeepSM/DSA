def largest_subarray_with_k_sum(arr, n, k):
    largest_subarray_length = 0
    current_sum = 0
    hash_map = dict()

    for idx in range(n):
        current_sum += arr[idx]
        if current_sum == k:
            largest_subarray_length = idx+1
        else:
            if current_sum in hash_map.keys():
                largest_subarray_length = max(largest_subarray_length, idx - hash_map[current_sum])
            else:            
                hash_map[current_sum] = idx
    return largest_subarray_length

if __name__ == '__main__':
    s = "-341 778 -826 -153 -574 -289 -993 -622 -989 -695 150 -692 755 -150 -586 -123 960 -182 -605 168 -635 47 -108 126 158 71 -584 -482 565 -51 369 -431 431 467 305 572 -793 276 639 -706 574 158 894 -849 979 -959 432 -25 712 -897 -476 661 791 880 -686 -278 364 -123 429 -65 230 459 -770 -872 330 -202 -944 783 -502 869 -246 -154 -935 572 959 -475 18 -198 -769"
    arr = list(map(int, s.split(" ")))
    n = len(arr)
    target_sum = 0
    print(largest_subarray_with_k_sum(arr, n, target_sum))