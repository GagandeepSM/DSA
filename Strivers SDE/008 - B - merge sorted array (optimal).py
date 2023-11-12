'''
Merge two sorted arrays without using extra space.
Time complexity : O(min(n, m)) + O(n*log(n)) + O(m*log(m))
Space complexity : O(1)
'''

def mergeSortedArray(arr1, arr2):
    leftPointer = len(arr1) - 1
    rightPointer = 0
    while leftPointer >= 0 and rightPointer < len(arr2):
        if arr1[leftPointer] > arr2[rightPointer]:
            arr1[leftPointer], arr2[rightPointer] = arr2[rightPointer], arr1[leftPointer]
            leftPointer -= 1   
            rightPointer += 1
        else:
            break
    arr1.sort()
    arr2.sort()
    return arr1 + arr2


if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [0, 2, 6, 8, 9]
    print(mergeSortedArray(arr1, arr2))