# https://leetcode.com/problems/find-the-highest-altitude
# easy
# daily
from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest_alt, cur_alt = 0, 0
        for diff in gain:
            cur_alt = cur_alt + diff
            highest_alt = max(highest_alt, cur_alt)
        return highest_alt
