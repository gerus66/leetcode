# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks
# medium
# daily
from typing import List


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        need = sorted([c - r for c, r in zip(capacity, rocks)])
        i, left = 0, additionalRocks
        while i < len(capacity) and left >= 0:
            i, left = i + 1, left - need[i]
            if left < 0:
                return i - 1
        return len(capacity)
