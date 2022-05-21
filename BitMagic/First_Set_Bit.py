class Solution:
    def getFirstSetBit(self,n):
        bitCount = 0
        for i in range(32):
            bitVal = (n >> i)&1
            if(bitVal):
                return i+1
        return 0
