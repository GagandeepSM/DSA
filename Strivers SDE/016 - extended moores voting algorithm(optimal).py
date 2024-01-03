'''
Extended Moore's Voting Algorithm (Optimal)
Time: O(n)
Space: O(1)
'''

def majorityElement(nums):
    count1 = 0
    count2 = 0
    first = 0
    second = 1
    for i in nums:
        if i == first:
            count1 += 1
        elif i == second:
            count2 += 1
        elif count1 == 0:
            first = i
            count1 = 1
        elif count2 == 0:
            second = i
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1
    count1 = 0
    count2 = 0
    for i in nums:
        if i == first:
            count1 += 1
        elif i == second:
            count2 += 1
    ans = []
    if count1 > len(nums)//3:
        ans.append(first)
    if count2 > len(nums)//3:
        ans.append(second)
    return ans

print(majorityElement([1,1,1,3,3,2,2,2])) # [1,2]
print(majorityElement([1,2])) # [1,2]
print(majorityElement([1])) # [1]
print(majorityElement([1,2,3])) # []
print(majorityElement([3,2,3])) # [3]
print(majorityElement([1,2,3,4])) # []
print(majorityElement([1,2,3,1,1])) # [1]
print(majorityElement([1,2,3,1,1,2])) # [1,2]
print(majorityElement([1,2,3,1,1,2,2])) # [1,2]
