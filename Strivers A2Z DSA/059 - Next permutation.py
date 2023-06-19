def nextPermutation(permutation, n):
    breakpoint = -1 # BREAKPOINT SET AT THE LAST INDEX

    #TRAVERSE BACKWARDS AND FIND THE BREAKPOINT
    for i in range(n-2, -1, -1):
        if permutation[i+1] > permutation[i]:
            breakpoint = i
            break
    else:
        return permutation[::-1]

    #SWAP THE BREAKPOINT ELEMENTS
    for i in range(n-1, breakpoint, -1):
        if permutation[breakpoint] < permutation[i]:
            permutation[breakpoint], permutation[i] = permutation[i], permutation[breakpoint]
            break
    
    permutation[breakpoint+1:] = reversed(permutation[breakpoint+1:])

    return permutation
