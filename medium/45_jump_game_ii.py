# https://leetcode.com/problems/jump-game-ii
# medium
# daily
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        min_steps = [len(nums)] * len(nums)
        min_steps[0], steps, max_distance = 0, 0, 0
        for i, num in enumerate(nums):
            for j in range(max_distance, i+num+1):
                if j < len(nums):
                    min_steps[j] = min(min_steps[j], min_steps[i]+1)
                    max_distance = j
                    if j == len(nums)-1:
                        return min_steps[-1]
