class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        squared_nums = [num**2 for num in nums]
        
        
        return list(sorted(squared_nums))