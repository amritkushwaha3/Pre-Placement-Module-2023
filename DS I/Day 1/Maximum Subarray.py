class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = []
        dp.append(nums[0])
        current_largest_sum = dp[0]
        for i in range(1, len(nums)):
            dp.append(max(dp[i-1] + nums[i], nums[i]))
            if dp[i] > current_largest_sum:
                current_largest_sum = dp[i]
        return current_largest_sum
        