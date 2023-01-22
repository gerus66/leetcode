# https://leetcode.com/problems/word-pattern
# easy
# practice - missed daily
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        ws = s.split(' ')
        if len(pattern) != len(ws):
            return False
        d, words = {}, set()
        for p, w in zip(list(pattern), ws):
            if p in d and d[p] != w:
                return False
            if p not in d and w in words:
                return False
            d[p] = w
            words.add(w)
        return True
    