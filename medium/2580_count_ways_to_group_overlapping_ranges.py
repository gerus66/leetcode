# https://leetcode.com/problems/count-ways-to-group-overlapping-ranges
# medium
# biweekly contest 99
from typing import List


class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        sr = sorted(ranges)
        groups, i = 0, 0
        while i < len(sr):
            end = sr[i][1]
            while i < len(sr) and sr[i][0] <= end:
                end = max(end, sr[i][1])
                i += 1
            groups += 1
        return 2**groups % (10**9 + 7)
    