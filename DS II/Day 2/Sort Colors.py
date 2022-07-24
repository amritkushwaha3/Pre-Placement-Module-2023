class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0 for i in range(0, 3)]
        
        for num in nums:
            colors[num] += 1
            
        current = 0
        for i in range(0, 3):
            for j in range(0, colors[i]):
                nums[current] = i
                current += 1