class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]*len(nums)
        for i in range(1, len(nums)):
            products[i] = products[i-1] * nums[i-1]
        total_num = 1
        for i in range(len(nums)-1,-1,-1):
            products[i] *= total_num
            total_num *= nums[i]
        return products