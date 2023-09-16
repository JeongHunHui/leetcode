class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_count = 0
        nums_len = len(nums)-1
        while nums_len > 0:
            for i in range(nums_len):
                num = nums[i]+i
                if num >= nums_len:
                    jump_count += 1
                    nums_len = i
                    break
        return jump_count