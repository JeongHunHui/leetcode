class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cond, count = nums[0], 1
        for num in nums[1:]:
            if num == cond:
                count += 1
            else:
                count -= 1
            if count == 0:
                cond = num
                count = 1
        return cond