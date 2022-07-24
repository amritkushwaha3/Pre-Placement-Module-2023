class Solution:
    def findMin(self, nums: List[int]) -> int:
        """Find minimum element in rotated sorted array.

        Args:
            nums (List[int]): Rotated sorted array

        Returns:
            int: Minimum value
        """
        left = 0
        center = len(nums) // 2
        right = len(nums) - 1

        while True:
            left_value = nums[left]
            center_value = nums[center]
            right_value = nums[right]
            if center - left <= 1 and right - center <= 1:
                return min(left_value, center_value, right_value)
            elif left_value < center_value < right_value:
                return left_value
            elif left_value > center_value:
                right = center
                center = center - (center - left) // 2
            elif center_value > right_value:
                left = center
                center = center + (right - center) // 2