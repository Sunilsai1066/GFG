class Solution:
    def countBitsFlip(self,a,b):
        bitFlip = 0
        for i in range(32):
            if((a >> i)&1 != (b >> i)&1):
                bitFlip += 1
        return bitFlip
