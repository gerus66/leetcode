# https://leetcode.com/problems/add-to-array-form-of-integer
# easy
# daily
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        i, res, kk = 0, [], k
        while kk and ((i := i + 1) <= len(num)):
            kk, cur = divmod(kk + num[-i], 10)
            res.append(cur)
        while kk:
            kk, cur = divmod(kk, 10)
            res.append(cur)
        return num[:-len(res)] + list(reversed(res))
