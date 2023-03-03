# https://leetcode.com/problems/minimum-average-difference
# medium
# practice - missed daily
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        sum1, sum2 = 0, sum(nums)
        min_diff, min_diff_i = sum2 // len(nums), len(nums) - 1
        for i, num in enumerate(nums[:-1]):
            sum1, sum2 = sum1 + num, sum2 - num
            cur_diff = abs(sum1 // (i+1) - sum2 // (len(nums)-i-1))
            if cur_diff < min_diff or cur_diff == min_diff and i < min_diff_i:
                min_diff, min_diff_i = cur_diff, i
        return min_diff_i
