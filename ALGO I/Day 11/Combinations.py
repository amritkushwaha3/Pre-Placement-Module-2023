class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        
        nums = [i for i in range(1, n + 1)]
        
        self.helper(nums, k, results, [], 0)
                
        return results
        
    def helper(self, nums, k, results, combination, start):
        if len(combination) == k:
            results.append(list(combination))
            return
        
        for i in range(start, len(nums)):
            num = nums[i]
            
            combination.append(num)
            self.helper(nums, k, results, combination, i + 1)
            combination.pop()