class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        before_product = [1 for i in range(len(nums))]
        
        after_product = [1 for i in range(len(nums))]
        
        
        for i in range(1, len(nums)):
            before_product[i] = before_product[i - 1] * nums[i - 1]
        
        
        for i in range(len(nums) - 2, -1, -1):
            after_product[i] = after_product[i + 1] * nums[i + 1]

            
        results = []
        
        for p1, p2 in zip(before_product, after_product):
            results.append(p1 * p2)
            
        return results