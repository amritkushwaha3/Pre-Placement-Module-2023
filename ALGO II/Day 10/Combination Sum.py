class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(cur, path):
            if cur == 0:
                res.append(path)
            for n in candidates:
                if n > cur:
                    break
                if path and n < path[-1]:
                    continue
                dfs(cur - n, path + [n])
                
        res = []
        candidates.sort()
        dfs(target, [])
        return res