'''
Reverse Pairs 
Given an array of integers nums, you need to find the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and
nums[i] > 2 * nums[j].
time complexity: O(nlogn)
space complexity: O(n)
'''

def merge(arr, low, mid, high):
    left = low
    right = mid+1
    temp = []
    while left <= mid  and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])            
            right += 1        
    while left <= mid:
        temp.append(arr[left])
        left += 1
    while right <= high:
        temp.append(arr[right])            
        right += 1
    
    for i in range(low, high+1):
        arr[i] = temp[i-low]

def count_reverse(arr, low, mid, high):
    count = 0
    right = mid + 1
    for i in range(low, mid+1):
        while right <= high and arr[i] > 2*arr[right]:
            right += 1
        count += (right - (mid + 1))
    return count 

def merge_sort(arr, low, high):
    count = 0
    if low >= high:
        return count
    mid = low + (high - low) // 2
    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid+1, high)
    count += count_reverse(arr, low, mid, high)
    merge(arr, low, mid, high)
    return count

arr = [5,4,3,2,1]
count = merge_sort(arr, 0, len(arr)-1)
print(count)