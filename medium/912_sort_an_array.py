# https://leetcode.com/problems/sort-an-array
# medium
# daily
from typing import List


class Solution:
    def s(self, x):
        if len(x) < 2:
            return x
        lf, rt = self.s(x[:len(x) // 2]), self.s(x[len(x) // 2:])
        i, j = 0, 0
        while i < len(lf) or j < len(rt):
            if i < len(lf) and (j >= len(rt) or lf[i] < rt[j]):
                x[i + j], i = lf[i], i + 1
            else:
                x[i + j], j = rt[j], j + 1
        return x

    def sortArray(self, nums: List[int]) -> List[int]:
        return self.s(nums)
