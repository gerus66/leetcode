# https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured
# easy
# biweekly contest 94 - virtual
from typing import List


class Solution:
    def captureForts(self, forts: List[int]) -> int:
        start, cur_length, max_length, prev = None, None, 0, forts[0]
        for f in forts[1:]:
            if f == 0:
                if prev == 1 or prev == -1:
                    start, cur_length = prev, 0
                cur_length = cur_length + 1 if cur_length is not None else None
            elif cur_length and start * f == -1:
                max_length = max(cur_length, max_length)
                start, cur_length = None, None
            else:
                start, cur_length = None, None
            prev = f
        return max_length
