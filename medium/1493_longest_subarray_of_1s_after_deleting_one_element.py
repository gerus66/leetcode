# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element
# medium
# daily
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_len, cur, prev, fl = 0, 0, 0, False
        for i, el in enumerate(nums):
            if el:
                cur += 1
            else:
                max_len, cur, prev, fl = max(max_len, prev+cur), 0, cur, True
        return max(max_len, prev+cur) - (0 if fl else 1)
