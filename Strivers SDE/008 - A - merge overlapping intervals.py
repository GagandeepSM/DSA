'''
    Merge Overlapping Intervals - Brute Force
    Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals. Let the intervals be represented as pairs of integers for simplicity.
    Time Complexity: O(n^2)
    Space Complexity: O(n)
'''

def mergeOverlappingIntervals(arr):
    arr.sort()
    n = len(arr)
    ans = []
    for i in range(n):
        start, end = arr[i][0], arr[i][1]

        if ans and end <= ans[-1][1]:
            continue
        
        for j in range(i+1, n):
            if arr[j][0] <= end:
                end = max(end, arr[j][1])
            else:
                break
        ans.append([start, end])
    return ans
        
if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(mergeOverlappingIntervals(intervals)) # [[1,6],[8,10],[15,18]]