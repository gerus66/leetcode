# https://leetcode.com/problems/delete-columns-to-make-sorted
# easy
# daily
from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        lowest = list(strs[0])
        for s in strs[1:]:
            for i, ch in enumerate(s):
                lowest[i] = ch if lowest[i] and lowest[i] <= ch else None

        return sum(k is None for k in lowest)
