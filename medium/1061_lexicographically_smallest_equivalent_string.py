# https://leetcode.com/problems/lexicographically-smallest-equivalent-string
# medium
# practice - missed daily
from collections import defaultdict


class Solution:
    def __init__(self):
        self.all = set()
        self.parts = defaultdict(set)

    def find_min(self, ch):
        if ch not in self.all:
            return ch
        for k, v in self.parts.items():
            if ch in v:
                return k

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        for c1, c2 in zip(s1, s2):
            if c1 == c2:
                continue
            chs = {c1, c2, self.find_min(c1), self.find_min(c2)}
            self.all.update({c1, c2})
            new_min = min(chs)
            self.parts[new_min].update(chs)
            for ch in chs:
                if ch != new_min:
                    self.parts[new_min].update(self.parts[ch])
                    self.parts.pop(ch)
        return ''.join(self.find_min(ch) for ch in baseStr)
