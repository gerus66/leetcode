# https://leetcode.com/problems/minimum-common-value
# easy
# biweekly contest 96
from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, n1, j, n2 = 0, len(nums1), 0, len(nums2)
        while i < n1 and j < n2:
            if nums1[i] == nums2[j]:
                return nums1[i]
            if nums1[i] < nums2[j]:
                i += 1
                continue
            if nums1[i] > nums2[j]:
                j += 1
        return -1
    