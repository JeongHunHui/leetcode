from collections import deque

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        new_nums = deque(nums)
        for _ in range(k):
            new_nums.appendleft(new_nums.pop())
        nums[:] = list(new_nums)
        