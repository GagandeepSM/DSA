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

def merge(arr, low, mid, high):
    temp = []
    i = low
    j = mid+1
    while i<=mid and j<=high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i+=1
        else:
            temp.append(arr[j])
            j+=1
    while i<=mid:
        temp.append(arr[i])
        i+=1
    while j<=high:
        temp.append(arr[j])
        j+=1

    for i in range(low, high+1):
        arr[i] = temp[i-low]
    

def merge_sort(arr, low, high):
    if low >= high:
        return
    mid = (low + high)//2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)

if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    low = 0
    high = len(arr)-1
    merge_sort(arr, low, high)
    print(arr)