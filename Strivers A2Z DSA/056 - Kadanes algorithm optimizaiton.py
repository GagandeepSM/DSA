'''
KADANES ALGORITHM
MAXIMUM SUM OF AN SUBARRAY

APPROACH 3: KADANES ALGORITHM OPTIMIZATION
    TC : O(N)
    SC : O(1)

'''

def kadanes_algorithm(arr, n):
    max_sum = -100000000
    start = 0
    temp_sum = 0
    ans_start,ans_end = 0,0 

    for i in range(n):
        if temp_sum ==0:
            start = i
        temp_sum += arr[i]
        
        if temp_sum > max_sum:
            max_sum = temp_sum
            ans_end = i
            ans_start = start
            
        if temp_sum < 0:
            temp_sum = 0
            
    return (ans_start, ans_end, temp_sum)
        
         
n = 9
arr = [1,2,7,-4,3,2,- 10,9,1]

r = kadanes_algorithm(arr, n)
print(arr[r[0]:r[1]+1], 'SUM =' ,r[2])
