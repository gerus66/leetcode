# https://leetcode.com/problems/jump-game
# medium
# daily
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        target = 0
        for i, elem in enumerate(nums[-1::-1]):
            if elem >= i - target:
                target = i
        return target == len(nums) - 1
    