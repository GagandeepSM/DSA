'''
KADANES ALGORITHM
MAXIMUM SUM OF AN SUBARRAY

APPROACH 1: BRUTE FORCE
    TC : O(N*3)
    SC : O(1)
    
APPROACH 2: OPTIMIZATION APPROACH 1
    TC : O(N*2)
    SC : O(1)

APPROACH 3: KADANES ALGORITHM
    TC : O()
    SC : O()

'''

def approach1(arr, n):
    max_sum = 0
    for i in range(n):
        for j in range(i, n):
            temp_sum = sum(arr[i:j])
##            print(arr[i:j], temp_sum)
            if temp_sum > max_sum:
                max_sum = temp_sum
    return max_sum

def approach2(arr, n):
    max_sum = -10000000
    for i in range(n):
        temp_sum = 0 
        for j in range(i,n):            
            temp_sum += arr[j]
            if temp_sum > max_sum:
                max_sum = temp_sum
    return max_sum

def approach3(arr, n):
    max_sum = -100000000
    temp_sum = 0
    for i in range(n):
        temp_sum += arr[i]
        if temp_sum > max_sum:
            max_sum = temp_sum
            
        if temp_sum < 0:
            temp_sum = 0
    return max_sum
        
        
         
n = 9
arr = [1,2,7,-4,3,2,- 10,9,1]

res1 = approach3(arr, n)
print(res1)
