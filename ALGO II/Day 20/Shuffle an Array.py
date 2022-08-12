class Solution:
  def __init__(self, nums: List[int]):
    self.nums = nums

  def reset(self) -> List[int]:
    """
    Resets the array to its original configuration and return it.
    """
    return self.nums

  def shuffle(self) -> List[int]:
    """
    Returns a random shuffling of the array.
    """
    A = self.nums.copy()
    for i in range(len(A) - 1, 0, -1):
      j = randint(0, i)
      A[i], A[j] = A[j], A[i]
    return A

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()