'''
Two Sum (Optimal)
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.You can return the answer in any order.
Time Complexity: O(n) + O(nlogn)
Space Complexity: O(1)
'''

def two_sum(arr, target):
    arr.sort()

    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return [left, right]
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

arr = [2, 7, 11, 15]
target = 9
print(two_sum(arr, target))
