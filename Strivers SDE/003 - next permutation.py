'''
Problem Statement: 
    Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
    If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).
    The replacement must be in place and use only constant extra memory.

Time Complexity: O(n)
Space Complexity: O(1)
'''

def next_permutation(arr):
    breakpoint = -1
    # FIND THE BREAKPOINT
    for i in range(len(arr)-2, -1, -1):
        if arr[i] < arr[i+1]:
            breakpoint = i
            break
    else:
        # IF BREAKPOINT IS NOT FOUND, REVERSE THE ARRAY
        arr.reverse()
        return arr
    
    # SWAP BOTH ELEMENTS
    for i in range(len(arr)-1, breakpoint, -1):
        if arr[i] > arr[breakpoint]:
            arr[i], arr[breakpoint] = arr[breakpoint], arr[i]
            break
    
    # REVERSE THE ARRAY FROM BREAKPOINT+1 TO END
    for i in range(breakpoint+1, len(arr)):
        if i >= len(arr) - i + breakpoint:
            break
        arr[i], arr[len(arr) - i + breakpoint] = arr[len(arr) - i + breakpoint], arr[i]
    return arr

if __name__ == '__main__':
    arr = [1, 2, 3]
    result = next_permutation(arr)
    print(result)