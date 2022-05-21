class Solution:
    def maxConsecutiveOnes(self, N):
        result = 0
        bitCount = 0
        for i in range(32):
            bitVal = (N >> i)&1
            if(bitVal):
                bitCount += 1
                result = max(result, bitCount)
            else:
                bitCount = 0
        return result
