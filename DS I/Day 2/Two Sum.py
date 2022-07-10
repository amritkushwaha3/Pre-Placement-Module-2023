class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        _dict = {}
        for i, num in enumerate(nums):
            if target-num in _dict.keys():
                return [_dict[target-num], i]
            else:
                _dict[num] = i