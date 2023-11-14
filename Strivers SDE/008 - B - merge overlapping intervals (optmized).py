'''
    Merge Overlapping Intervals - Optimized Approach
    Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals. Let the intervals be represented as pairs of integers for simplicity.
    Time Complexity: O(nlogn)
    Space Complexity: O(n)
'''

def mergeOverlappingIntervals(arr):
    arr.sort()
    ans = []
    n = len(arr)
    for i in range(n):
        start, end = arr[i][0], arr[i][1]
        if ans and end <= ans[-1][1]:
            continue
        if ans  and start <= ans[-1][1]:
            ans[-1][1] = end
        else:
            ans.append([start, end])
    return ans
   
if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(mergeOverlappingIntervals(intervals)) # [[1,6],[8,10],[15,18]]