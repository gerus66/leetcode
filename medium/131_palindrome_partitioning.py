# https://leetcode.com/problems/palindrome-partitioning
# medium
# daily
from typing import List
import itertools


class Solution:
    @staticmethod
    def is_palindrom(s):
        return all(s[i] == s[-(i+1)] for i in range(len(s)//2))

    def partition(self, s: str) -> List[List[str]]:
        d = {ch: {tuple(ch)} for ch in s}
        for width in range(2, len(s) + 1):
            for i_st in range(0, len(s) - width + 1):
                substr = s[i_st:i_st + width]
                if d.get(substr) is not None:
                    continue
                d[substr] = set()
                for i_middle in range(1, len(substr)):
                    it = itertools.product(d[substr[:i_middle]], d[substr[i_middle:]])
                    d[substr] |= {x[0] + x[1] for x in it}
                if self.is_palindrom(substr):
                    d[substr].add(tuple([substr]))
        return [list(t) for t in d.get(s)]
