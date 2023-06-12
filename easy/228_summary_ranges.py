# https://leetcode.com/problems/summary-ranges
# easy
# daily
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res, st = [], None
        for i, x in enumerate(nums):
            if st is None:
                st = x
            elif x - nums[i-1] > 1:
                res.append(str(st) if st == nums[i-1] else f'{st}->{nums[i-1]}')
                st = x
        if st is not None:
            res.append(str(st) if st == nums[-1] else f'{st}->{nums[-1]}')
        return res
    