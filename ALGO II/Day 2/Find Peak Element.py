class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        
        start = 0
        end = len(nums) - 1
        
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                end = mid
            elif nums[mid] < nums[mid + 1]:
                start = mid
                
        if nums[end] > nums[start]:
            return end
        
        return start