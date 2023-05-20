"""
APPROACH 1: BRUTE FORCE
  T(C) : O(N) + O(N/2)
  S(C) : O(N) 

APPROACH 2: OPTIMAL APPROACH
    T(C) : O(N) 
    S(C) : O(N) 

"""
def alternateNumbers(a):
    # Write your code here.
    pi,ni = 0,1
    n_arr = [0] * len(a)  
    for el in a:
        if el<0:
            n_arr[ni] = el
            ni+=2
        else:
            n_arr[pi] = el
            pi+=2
    return n_arr

s ="1 2 -3 -1 -2 3"
S = list(map(int, s.split(" ")))
print(alternateNumbers(S))
