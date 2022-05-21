class Solution:
    def isSparse(self,n):
        bitCount = 0
        for i in range(32):
            bitVal = (n >> i)&1
            if(bitVal):
                bitCount += 1
                if(bitCount >= 2):
                    return 0
            else:
                bitCount = 0
        return 1
