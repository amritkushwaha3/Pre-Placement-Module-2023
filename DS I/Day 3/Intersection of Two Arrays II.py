class Solution(object):
   def intersect(self, nums1, nums2):
      """
      :type nums1: List[int]
      :type nums2: List[int]
      :rtype: List[int]
      """
      m = {}
      if len(nums1)<len(nums2):
         nums1,nums2 = nums2,nums1
      for i in nums1:
         if i not in m:
            m[i] = 1
         else:
            m[i]+=1
      result = []
      for i in nums2:
         if i in m and m[i]:
            m[i]-=1
            result.append(i)
      return result
ob1 = Solution()
print(ob1.intersect([1,4,5,3,6], [2,3,5,7,9]))