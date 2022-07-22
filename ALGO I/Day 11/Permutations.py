class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        visited = set()
        self.helper(results, nums, [], 0, visited)
        
        return results
    
    def helper(self, results, nums, combination, start, visited):
        if len(combination) == len(nums):
            results.append(list(combination))
            return
        
        
        for i in range(len(nums)):
            if nums[i] in visited:
                continue
            
            visited.add(nums[i])
            combination.append(nums[i])
            self.helper(results, nums, combination, i + 1, visited)
            combination.pop()            
            visited.remove(nums[i])