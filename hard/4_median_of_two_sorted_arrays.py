# https://leetcode.com/problems/median-of-two-sorted-arrays
# hard
# daily mock interview

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        to_cut = (len(nums1) + len(nums2) - 1) // 2
        left, right = nums1, nums2

        while to_cut and left and right:
            half = to_cut // 2 or 1
            if left[min(half, len(left)) - 1] > right[min(half, len(right)) - 1]:
                left, right = right, left

            cutted = min(half, len(left))
            left, to_cut = left[cutted:], to_cut - cutted

        if left and right:
            if left[0] > right[0]:
                left, right = right, left
            mds = [left[0], left[1] if len(left) > 1 and left[1] < right[0] else right[0]]
        else:
            mds = left if left else right
            mds = mds[to_cut:to_cut + 2]

        return mds[0] if (len(nums1) + len(nums2)) % 2 else sum(mds) / 2
