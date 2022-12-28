# https://leetcode.com/problems/maximum-tastiness-of-candy-basket
# medium
# practice missed contest - weekly 325 virtual
from typing import List


class Solution:
    def __init__(self):
        self.prices = []

    def try_diff(self, diff, k):
        n, nxt = 1, self.prices[0]+diff
        for p in self.prices[1:]:
            if p >= nxt:
                n, nxt = n+1, p+diff
            if n == k:
                return True
        return False

    def maximumTastiness(self, price: List[int], k: int) -> int:
        self.prices = price
        self.prices.sort()
        st, fin = 0, price[-1] - price[0]
        while st < fin:
            try_diff = st + (fin-st)//2
            if self.try_diff(try_diff, k):
                st = try_diff + 1
            else:
                fin = try_diff - 1
        return st if self.try_diff(st, k) else st - 1
