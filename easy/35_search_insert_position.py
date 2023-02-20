# https://leetcode.com/problems/search-insert-position
# easy
# daily
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lf, rt = 0, len(nums)
        while lf != rt:
            mid = (lf + rt) // 2
            if nums[mid] == target:
                return mid
            if lf == mid:
                return lf if target < nums[lf] else rt
            lf, rt = (mid, rt) if nums[mid] < target else (lf, mid)
