'''
Count inversions in an array
Time Complexity: O(nlogn)
Space Complexity: O(n)
'''

def merge(arr, low, mid, high):
    left = low
    right = mid + 1
    temp = []
    count  = 0
    while left <= mid  and right <= high:
        if arr[left] <= arr[high]:
            temp.append(arr[left])
            left += 1
        else:
            count += mid - left + 1
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
    return count

def merge_sort(arr, low, high):
    count = 0
    if low >= high:
        return count
    mid = (low + high) // 2
    count += merge_sort(arr, low, mid)
    count += merge_sort(arr, mid+1, high)
    count += merge(arr, low, mid, high)
    return count

def count_inversions(arr):
    low = 0
    high = len(arr)-1
    return merge_sort(arr, low, high)

if __name__ == "__main__":
    arr = [52244275, 123047899,493394237,922363607,378906890,188674257,222477309,902683641,860884025,339100162]
    result = count_inversions(arr) # 
    print(result) # 