# https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray
# medium
# contest biweekly 112
from collections import Counter
from typing import List


class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        cur_dict = Counter(nums[:k])
        max_sum = sum(nums[:k]) if len(cur_dict.keys()) >= m else 0

        i_fin = k
        while i_fin < len(nums):
            drop = nums[i_fin - k]
            cur_dict[drop] -= 1
            if cur_dict[drop] == 0:
                cur_dict.pop(drop)

            add = nums[i_fin]
            cur_dict[add] = cur_dict.get(add, 0) + 1

            i_fin += 1
            if len(cur_dict.keys()) >= m:
                max_sum = max(max_sum, sum(nums[i_fin - k:i_fin]))

        return max_sum
