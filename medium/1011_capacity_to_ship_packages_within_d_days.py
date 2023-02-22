# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days
# medium
# daily
from typing import List
import math


class Solution:
    @staticmethod
    def fill_ship(weights, capacity):
        days, cur_ship = 1, 0
        for w in weights:
            if w > capacity:
                return math.inf
            if cur_ship + w > capacity:
                days, cur_ship = days + 1, 0
            cur_ship += w
        return days

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lf, rt = 1, sum(weights)
        while True:
            mid = (lf + rt) // 2
            if lf == mid:
                return rt
            lf, rt = (mid, rt) if self.fill_ship(weights, mid) > days else (lf, mid)
