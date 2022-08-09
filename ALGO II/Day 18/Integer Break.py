class Solution:
    def integerBreak(self, n: int) -> int:
        #First deal with the case where n is less than or equal to 3
        if n <= 3:
            return n-1
        
        #First split, determine the quantity and the remainder
        a = n // 3
        b = n % 3

        #Call here math.pow () method, which calls the pow function of the underlying C library, is more efficient
        import math
        #Average score directly returns 3 ^ a
        if b == 0:
            return int(math.pow(3, a))
        elif b == 1:
            return int(math.pow(3, a-1) * 4)
        #The rest is the situation of the remaining two
        return int(math.pow(3, a) * 2)