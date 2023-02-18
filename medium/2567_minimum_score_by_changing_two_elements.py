# https://leetcode.com/problems/minimum-score-by-changing-two-elements
# medium
# biweekly 98
from typing import List


class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        mins, maxs = [10**9+1]*3, [0]*3
        for n in nums:
            for i in range(3):
                if n < mins[i]:
                    mins = mins[:i] + [n] + mins[i:-1]
                    break
            for i in range(3):
                if n > maxs[i]:
                    maxs = maxs[:i] + [n] + maxs[i:-1]
                    break
        return min(maxs[1]-mins[1], maxs[0]-mins[2], maxs[2]-mins[0])
