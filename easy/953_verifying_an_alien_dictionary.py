# https://leetcode.com/problems/verifying-an-alien-dictionary
# easy
# daily
from typing import List


class Solution:
    @staticmethod
    def right_order_2(w1, w2, d):
        for i, ch in enumerate(w1):
            if i >= len(w2) or d[ch] > d[w2[i]]:
                return False
            if d[ch] < d[w2[i]]:
                return True
        return True

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        d = {ch: i for i, ch in enumerate(order)}
        for i in range(1, len(words)):
            if not self.right_order_2(words[i-1], words[i], d):
                return False
        return True
