class Solution:
    def canJump(self, nums: List[int]) -> bool:
                
        max_jump = nums[0]
        
        for i in range(1, len(nums)): 
            if max_jump < i:
                return False            
            elif i + nums[i] > max_jump:
                max_jump = i + nums[i]                
           
        return True