# https://leetcode.com/problems/maximum-ice-cream-bars
# medium
# daily
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ice_creams, money, bars = sorted(costs), coins, 0
        for ice in ice_creams:
            bars, coins = bars + 1, coins - ice
            if coins < 0:
                return bars - 1
        return bars
    