'''
Merge two sorted array's : Brute Force
Time complexity : O(n+m)
Space complexity : O(n+m)
'''
def mergeTwoArrays(array1, array2):
    i = 0
    j = 0
    array3 = []
    while i < len(array1) and j < len(array2):
        if array1[i] < array2[j]:
            array3.append(array1[i])
            i += 1
        else:
            array3.append(array2[j])
            j += 1
    while i < len(array1):
        array3.append(array1[i])
        i += 1
    while j < len(array2):
        array3.append(array2[j])
        j += 1
    return array3


if __name__ == "__main__":
    array1 = [1, 3, 5, 7]
    array2 = [0, 2, 6, 8, 9]
    print(mergeTwoArrays(array1, array2))
