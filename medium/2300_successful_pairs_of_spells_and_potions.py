# https://leetcode.com/problems/successful-pairs-of-spells-and-potions
# medium
# daily
from typing import List
import bisect
import math


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        p, n = sorted(potions), len(potions)
        return [n - bisect.bisect_left(p, math.ceil(success/s)) for s in spells]
