class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        max_len = 2
        num_dict = {}
        for num in nums:
            if num in num_dict:
                num_dict[num] += 1
            else:
                num_dict[num] = 1
        keys = sorted(num_dict.keys())
        answer = []
        for key in keys:
            count = num_dict[key]
            count = max_len if count > max_len else count
            answer += [key]*count
        nums[:] = answer
        return len(nums)