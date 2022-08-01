class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        
        visited = set()
        self.helper(results, nums, [], visited)
        
        return results
    
    def helper(self, results, nums, permutation, visited):
        if len(permutation) == len(nums):
            if permutation not in results:
                results.append(list(permutation))
            return
        
        
        for i in range(len(nums)):
            if i in visited:
                continue

            permutation.append(nums[i])
            visited.add(i)

            self.helper(results, nums, permutation, visited)

            permutation.pop()
            visited.remove(i)