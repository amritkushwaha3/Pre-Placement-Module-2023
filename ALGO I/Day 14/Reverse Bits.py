class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        
        for _ in range(32):
            reverse = reverse << 1
            reverse += n & 1
            n = n >> 1
        
        return reverse