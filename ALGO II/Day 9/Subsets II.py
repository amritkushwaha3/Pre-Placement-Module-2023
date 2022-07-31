class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums = sorted(nums)

        self.helper(results, [], 0, nums)
        
        return results
    
    def helper(self, results, combination, start, nums):
        if combination not in results:
            results.append(list(combination))
        
        for i in range(start, len(nums)):
            combination.append(nums[i])            
            self.helper(results, combination, i + 1, nums)            
            combination.pop()