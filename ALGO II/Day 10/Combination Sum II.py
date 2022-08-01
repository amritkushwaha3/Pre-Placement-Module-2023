class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        candidates = sorted(candidates)
        self.helper(results, candidates, target, [], 0)
        
        return results
        
    def helper(self, results, candidates, target, combination, start):
        if target == 0:
            results.append(list(combination))
    
            return
        
        if target < 0:
            return
        
        for i in range(start, len(candidates)):
            if i != start and candidates[i] == candidates[i - 1]:
                continue
            
            combination.append(candidates[i])
            self.helper(results, candidates, target - candidates[i], combination, i + 1)
            combination.pop()