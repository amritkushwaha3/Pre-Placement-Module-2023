class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        num, count = Counter(nums).most_common(1)[0]
        return num