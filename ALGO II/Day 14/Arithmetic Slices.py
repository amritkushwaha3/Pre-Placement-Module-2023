class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        results = []
        
        for i in range(len(nums) - 1):
            prev = nums[i]
            
            diff = None
            
            subarrays = [nums[i]]
            
            
            for j in range(i + 1, len(nums)):
                if diff == None:
                    diff = nums[j] - prev
                    prev = nums[j]
                    subarrays.append(nums[j])
                else:              
                    if nums[j] - prev == diff:
                        subarrays.append(nums[j])
                        prev = nums[j]
                        
                        if len(subarrays) >= 3:
                            results.append(list(subarrays))                                            
                    else:
                        break
        
                
        return len(results)