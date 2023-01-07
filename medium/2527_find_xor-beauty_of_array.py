# https://leetcode.com/problems/find-xor-beauty-of-array
# medium
# biweekly contest 95
from typing import List


class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans = nums[0]
        for n in nums[1:]:
            ans = ans ^ n
        return ans
