# https://leetcode.com/problems/single-element-in-a-sorted-array
# medium
# daily
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lf, rt, n = 0, len(nums) - 1, len(nums)
        while True:
            mid = (lf + rt) // 2
            if ((mid == 0 or nums[mid-1] != nums[mid]) and
                (mid == n-1 or nums[mid] != nums[mid+1])):
                return nums[mid]
            if lf == mid:
                return nums[rt]
            if bool(mid % 2) != (nums[mid] == nums[mid+1]):
                lf, rt = mid, rt
            else:
                lf, rt = lf, mid
