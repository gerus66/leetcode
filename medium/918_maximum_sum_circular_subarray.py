# https://leetcode.com/problems/maximum-sum-circular-subarray
# medium
# practice - missed daily
from typing import List


class Solution:
    @staticmethod
    def max_subarray(arr):
        n = len(arr)
        left_sum, i_fin, cur_sum, max_sum = 0, 1, arr[0], arr[0]
        while i_fin < n:
            i_fin += 1
            cur_sum += arr[i_fin - 1]
            left_sum += arr[i_fin - 2]
            if left_sum < 0:
                cur_sum -= left_sum
                left_sum = 0
            max_sum = max(max_sum, cur_sum)
        return max(max_sum, cur_sum)

    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        if all(x < 0 for x in nums):
            return max(nums)

        rev = [-x for x in nums]
        return max(self.max_subarray(nums), sum(nums) + self.max_subarray(rev))
