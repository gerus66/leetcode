# https://leetcode.com/problems/kth-missing-positive-number
# easy
# daily
from typing import List


class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        for i, a in enumerate(arr, start=1):
            if a - i >= k:
                return k + i - 1
        return k + len(arr)
    