class Solution(object):
   def increasingTriplet(self, nums):
      small,big = 100000000000000000000,100000000000000000000
      for i in nums:
         if i <= small:
            small = i
         elif i<=big:
            big = i
         else :
            return True
      return False
ob1 = Solution()
print(ob1.increasingTriplet([5,3,8,2,7,9,4]))