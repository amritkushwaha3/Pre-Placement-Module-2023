class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # approach: use a set to save all encountered numbers

        occurrence_set = set()
        current = n
        while current != 1:
            current = self.digit_square(current)
            if current in occurrence_set: return False
            occurrence_set.add(current)

        return True

    def digit_square(self, num):
        base = 1
        result = 0
        while num % base < num:
            digit = num // base % 10
            result += digit * digit
            base *= 10

        return result