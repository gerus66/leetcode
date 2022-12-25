# https://leetcode.com/problems/longest-subsequence-with-limited-sum
# easy
# daily
from typing import List
import bisect


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        sub_sums = [0]
        for num in sorted(nums):
            sub_sums.append(sub_sums[-1] + num)

        return [bisect.bisect(sub_sums, q) - 1 for q in queries]
    