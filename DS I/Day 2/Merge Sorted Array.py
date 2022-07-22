class Solution:
    def merge(self, nums1, m, nums2, n):
        i=0
        for x in range(len(nums1)):
            if i>=n:
                break
            if nums1[x]==0:
                nums1[x]=nums2[i]
                i+=1           
        nums1.sort()        