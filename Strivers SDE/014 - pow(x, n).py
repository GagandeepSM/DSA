'''
Program to calculate power of x raised to n
Time complexity: O(logn)
Space complexity: O(1)
'''

class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        if n < 0:
            n = -n
            x = 1 / x
        while n > 0:
            if n % 2 == 0:
                n = n // 2
                x = x * x
            else:
                n = n - 1
                ans = ans * x
        return ans

ans = Solution().myPow(2.00000, 10)
print(ans)
