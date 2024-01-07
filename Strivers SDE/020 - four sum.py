'''
Four Sum: Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
    1. 0 <= a, b, c, d < n
    2. a, b, c, and d are distinct.
    3. nums[a] + nums[b] + nums[c] + nums[d] == target
    4. You may return the answer in any order.
Time Complexity: O(n^3)
Space Complexity: O(1)
'''

def four_sum(arr, target):
    arr.sort()
    ans = []
    n = len(arr)
    for i in range(n - 3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i + 1, n - 2):
            if j> i+1 and arr[j] == arr[j-1]:
                continue
            left = j + 1
            right = n - 1
            while left < right:
                if arr[i] + arr[j] + arr[left] + arr[right] == target:
                    ans.append([arr[i], arr[j], arr[left], arr[right]])
                    left += 1
                    right -= 1
                    while left < right and arr[left] == arr[left-1]:
                        left += 1
                    while left < right and arr[right] == arr[right+1]:
                        right -= 1
                elif arr[i] + arr[j] + arr[left] + arr[right] < target:
                    left += 1
                else:
                    right -= 1

    # Remove duplicates python way
    # ans = list(set(tuple(i) for i in ans))
    return ans


arr = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target = 9
print(four_sum(arr, target))
