# https://leetcode.com/problems/flip-string-to-monotone-increasing
# medium
# practice - missed daily
from collections import Counter


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        min_swaps = Counter(s)['0']  # swap all 0 to 1
        alt_swaps = min_swaps
        for ch in s:
            alt_swaps += 1 if ch == '1' else -1
            min_swaps = min(min_swaps, alt_swaps)
        return min_swaps
