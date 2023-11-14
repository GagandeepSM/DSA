'''
Find missing and duplicate value in an array : Optimal style
Time complexity:  O(n)
Space complexity: O(1)
'''

def findMissingRepeatingNumbers(arr: [int]) -> [int]:
    n = len(arr)
    naturalSum = (n * (n+1)) // 2 # sum of first n natural numbers
    naturalSquares = (n * (n+1) * (2*n+1)) // 6 # sum of squares of first n natural numbers
    currentSum = 0
    currentSquares = 0
    for i in range(n):
        currentSum += arr[i] # sum of array elements
        currentSquares += arr[i] * arr[i] # sum of squares of array elements 
    
    value1 = currentSum - naturalSum # x - y
    value2 = currentSquares - naturalSquares # x2 - y2
    value3 = value2 // value1 # x + y
    x = (value1 + value3) // 2 # Adding value1 and value3 gives 2x
    y = x - value1
    return [x, y]

if __name__ == "__main__":
    arr = [1, 3, 4, 5, 5, 6, 2]
    print(findMissingRepeatingNumbers(arr)) # [5, 7]