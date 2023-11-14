'''
Find missing and duplicate value in an array : Brute force style
Time complexity:  O(n^2)
Space complexity: O(1)
'''

def findMissingAndDuplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                duplicate = arr[i]
                break
    for i in range(1, len(arr)+1):
        if i not in arr:
            missing = i
            break
    return [duplicate, missing]

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 6, 6]
    print(findMissingAndDuplicate(arr))