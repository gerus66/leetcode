# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
# medium
# daily
from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        state = [0, -prices[0]]  # empty, full
        for p in prices[1:]:
            state = [max(state[0], state[1]+p-fee), max(state[1], state[0]-p)]
        return max(state)


# 0 -> 0
# 0 -> 1 -cost
# 1 -> 0 cost-fee
# 1 -> 1
