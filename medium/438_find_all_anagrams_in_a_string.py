# https://leetcode.com/problems/find-all-anagrams-in-a-string
# medium
# daily
from typing import List
from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d1, i, window, indexes = Counter(p), 0, 0, []
        while i < len(s):
            if window == len(p) and all(v == 0 for v in d1.values()):
                indexes.append(i-window)
            if s[i] in d1:
                d1[s[i]] -= 1
            window += 1
            if window > len(p):
                if s[i-window+1] in d1:
                    d1[s[i-window+1]] += 1
                window -= 1
            i += 1
        if window == len(p) and all(v == 0 for v in d1.values()):
                indexes.append(len(s)-window)
        return indexes
