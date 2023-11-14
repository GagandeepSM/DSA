
'''
NAME   : Two-Sum problem
PROBLEM: Find all the pairs that exists in the Array which equals target

APPROACH 1: Brute Force
    Time complexity  -> O(n^2)
    Space complexity -> O(1)
    
APPROACH 2: Two Pointer Approach
    Time complexity  -> O(nlogn)
    Space complexity -> O(n)

APPROACH 3: Hashing
    Time complexity  -> O(n)
    Space complexity -> O(n)
'''


def approach1(arr, target):
    result = list()
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                result.append(tuple(sorted([i,j])))
    return sorted(list(set(result)))

def approach2(arr, target):
    arr.sort()
    result = list()
    pointer1,pointer2 = 0,len(arr)-1
    
    while pointer1 < pointer2:
        if arr[pointer1] + arr[pointer2] < target:
            pointer1 += 1
        elif arr[pointer1] + arr[pointer2] > target:
            pointer2 -= 1
        else:
            result.append((arr[pointer1], arr[pointer2]))
            print(pointer1,pointer2)
            if pointer1 + 1 < pointer2 and arr[pointer1 + 1] == arr[pointer1]:
                pointer1 += 1
            else:
                pointer2 -= 1
    return result

def approach3(arr,target):
    pass

if __name__ == '__main__':
    
    arr = [2,2,2,2]
    target = 4
    
    res1 = approach1(arr, target)
    print('A1', res1)

    res2 = approach2(arr,target)
    print('A2', res2)
    
    res3 = approach3(arr,target)
    print('A3', res3)
