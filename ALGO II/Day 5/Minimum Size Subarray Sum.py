class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        j = 0
        current_sum = 0
        min_length = float(inf)
        
        for i in range(len(nums)):
            
            while current_sum < target and j < len(nums):                
                current_sum += nums[j]                
                j += 1
                
            if current_sum >= target:
                min_length = min(min_length, j - i)
                
            current_sum -= nums[i]
        
        if min_length == float(inf):
            return 0
            
        return min_length