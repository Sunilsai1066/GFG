class Solution:
    def posOfRightMostDiffBit(self,m,n):
        for i in range(31):
            if((m >> i)&1 != (n >> i)&1):
                return i+1
        return -1
