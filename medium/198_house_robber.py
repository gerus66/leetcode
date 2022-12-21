# https://leetcode.com/problems/house-robber
# medium
# training - missed daily
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        rows = []
        i = len(nums)
        row_length = 2
        while i >= 0:
            rows.append([nums[k] if k >= 0 else 0 for k in range(i-row_length, i)])
            i -= 2
            row_length += 1

        maxes = [0]*len(rows[-1])
        for ro in rows[::-1]:
            upd_ro = [k + l for k, l in zip(maxes, ro)]
            maxes = [max(upd_ro[k], upd_ro[k+1]) for k in range(0, len(upd_ro)-1)]
        return maxes[0]
