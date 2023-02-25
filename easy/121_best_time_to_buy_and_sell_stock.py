# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# easy
# daily
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, profit = prices[0], 0
        for p in prices:
            profit = p - buy if p - buy > profit else profit
            buy = p if p < buy else buy
        return profit
