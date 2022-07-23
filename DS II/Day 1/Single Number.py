class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        for key, value in count.items():
            if value == 1:
                return key