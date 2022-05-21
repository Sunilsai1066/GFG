class Solution:
    def isPowerofTwo(self,n):
        if(n == 0):
            return False
        val = n & (n-1)
        return val == 0
