# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
# medium
# daily
from typing import List


class Solution:
    def maxProfit(self, p: List[int]) -> int:
        d = [0]*5 + [p[i]-p[i-1] for i in range(1,len(p))] + [0]*4
        for i in range(4, len(p)+8):
            d[i] = max(max(d[i-4:i-1]), d[i-1] + d[i])
        return d[-1]
    