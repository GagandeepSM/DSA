'''
FIND MAJORITY ELEMENT - MOORE' VOTING ALGORITHM

APPROACH 1: BRUTE FORCE
    T(C) : O(N*N)
    S(C) : O(1)
    
APPROACH 2: HASHING
    T(C) : 2 * O(N)
    S(C) : O(N)

APPROACH 3: MOORES VOTING ALGORITHM
    T(C) : O(N) + O(N)
    S(C) : O(1)

'''

def approach1(arr, n):
    """
    BRUTEFORCE FOR EVERY ELEMENT
    IF COUNT > N/2 RETURN ELEMENT
    """
    pass


def approach2(arr, n):
    """ HASHING """
    h_map = dict()
    for key in arr:
        h_map[key] = h_map.get(key, 0) + 1        
    for k,v in h_map.items():
        if v > n//2:
            return k
    return -1

def approach3(arr, n):
    """ MOORES VOTING ALGORITHM """    
    element = -1
    count = 0
    for key in arr:
        if count == 0:
            count = 1
            element = key
        elif key == element:
            count += 1
        else:
            count -= 1
    
    occurance = arr.count(element)
    if occurance > n//2:
        return element
    return -1


""" DRIVER CODE """

n = 7
arr = [2,2,2,1,1,1]
result = approach3(arr, n)
print(result)
