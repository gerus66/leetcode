# https://leetcode.com/problems/sort-characters-by-frequency
# medium
# practice - missed daily
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        d = Counter(s)
        sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        s = [v*k for k, v in sorted_d]
        return ''.join(s)
