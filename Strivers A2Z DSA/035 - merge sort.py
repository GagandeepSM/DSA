'''
Merge sort is a divide and conquer algorithm. 
It divides the input array into two halves, 
calls itself for the two halves, and then merges the two sorted halves. 
The merge() function is used for merging two halves. 
The merge(arr, l, m, r) is a key process that assumes that arr[l..m] and arr[m+1..r] 
are sorted and merges the two sorted sub-arrays into one.

Time Complexity: O(nlogn)
Space Complexity: O(n)
'''

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * n1
    R = [0] * n2

    # copy data to temp arrays L[] and R[]
    for i in range(n1):
        L[i] = arr[l + i]
    
    for j in range(n2):
        R[j] = arr[m + 1 + j]
    
    # merge the temp arrays back into arr[l..r]
    i = 0 # initial index of first subarray
    j = 0 # initial index of second subarray
    k = l # initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            # if L[i] is smaller than or equal to R[j], 
            # then it will be copied to arr[k] first
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        
        k += 1
    
    # copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    
    # copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l = 0, r = None):
    if r is None:
        r = len(arr) - 1
    
    if l < r:
        # find the middle point
        m = (l + (r - 1)) // 2

        # sort first and second halves
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)

        # merge the sorted halves
        merge(arr, l, m, r)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    merge_sort(arr)
    print(arr)