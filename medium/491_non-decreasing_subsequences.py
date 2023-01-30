# https://leetcode.com/problems/non-decreasing-subsequences
# medium
# practice - missed daily
from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        d = {i: {(n,)} for i, n in enumerate(nums)}
        for i in range(1, len(nums)):
            for j in range(i):
                new_t = {prev+(nums[i],) for prev in d[j] if nums[i] >= prev[-1]}
                d[i].update(new_t)
        res = set()
        for arr in d.values():
            for a in arr:
                if len(a) > 1:
                    res.add(a)
        return [list(r) for r in res]
