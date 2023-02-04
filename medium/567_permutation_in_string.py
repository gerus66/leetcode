# https://leetcode.com/problems/permutation-in-string
# medium
# daily
from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1, i, window = Counter(s1), 0, 0
        while i < len(s2):
            if window == len(s1) and all(v == 0 for v in d1.values()):
                return True
            if s2[i] in d1:
                d1[s2[i]] -= 1
            window += 1
            if window > len(s1):
                if s2[i - window + 1] in d1:
                    d1[s2[i - window + 1]] += 1
                window -= 1
            i += 1
        return window == len(s1) and all(v == 0 for v in d1.values())
