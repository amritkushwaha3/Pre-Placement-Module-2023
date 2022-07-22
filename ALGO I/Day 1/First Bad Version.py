# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1: return 1;
        begin=1
        end=n
        while begin<end:
            mid=begin+(end-begin)/2
            if isBadVersion(mid): end=mid
            else: begin=mid+1
        return int(begin)
        