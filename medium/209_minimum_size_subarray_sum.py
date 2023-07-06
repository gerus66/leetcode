# https://leetcode.com/problems/minimum-size-subarray-sum
# medium
# daily
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0

        min_len, cur_len = len(nums), 1
        i_left, i_right, cur_sum = 0, 1, nums[0]
        while i_right < len(nums):
            while cur_sum < target and i_right < len(nums):
                i_right, cur_len = i_right + 1, cur_len + 1
                cur_sum += nums[i_right-1]
            if cur_sum >= target:
                min_len = min(min_len, cur_len)
            while cur_sum >= target:
                cur_sum -= nums[i_left]
                i_left, cur_len = i_left + 1, cur_len - 1
            min_len = min(min_len, cur_len+1)
        return min_len
    