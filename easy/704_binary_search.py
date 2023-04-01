# https://leetcode.com/problems/binary-search
# easy
# daily
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lf, rt = 0, len(nums) - 1
        while nums[rt] != target:
            mid = (lf + rt) // 2
            if nums[mid] == target:
                return mid
            if mid == lf:
                return -1
            lf, rt = (lf, mid) if target < nums[mid] else (mid, rt)
        return rt
    