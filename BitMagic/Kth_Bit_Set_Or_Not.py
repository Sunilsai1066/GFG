class Solution:
    def checkKthBit(self, n,k):
        Res = n & (1 << k)
        return True if Res else False
