'''
Moore's Voting Algorithm 
------------------------
Given an array of size n, find the majority element. The majority element is the element that appears more than n/2 times.
You may assume that the array is non-empty and the majority element always exist in the array.
Optimal Approach:
Time complexity: O(n)
Space complexity: O(1)
'''

def majorityElement(arr: [int]) -> int:
    count = 0
    candidate = None
    for num in arr:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    return candidate

if __name__ == "__main__":
    arr = [1,1,1,1,2,3,4,5,6,7,8,9,10]
    print(majorityElement(arr)) # 1 
    arr = [1,2,3,4,5,6,7,8,9,10]
    print(majorityElement(arr)) # None
    arr = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,2]
    print(majorityElement(arr)) # 2
    arr = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3]
    print(majorityElement(arr)) # 2
    arr = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3]
    print(majorityElement(arr)) # None
    arr = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3]
    print(majorityElement(arr)) # 2
    arr = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3]
    print(majorityElement(arr)) # None
    arr = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3]
    print(majorityElement(arr)) # 2
    arr = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3]
    print(majorityElement(arr)) # 3
    arr = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4]
    print(majorityElement(arr)) # None
    arr = [1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,4,4]   