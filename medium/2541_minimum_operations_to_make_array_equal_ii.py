# https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii
# medium
# practice missed
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        diffs = [a1-a2 for a1, a2 in zip(nums1, nums2)]
        if k == 0:
            return -1 if any(diffs) else 0
        if sum(diffs) or any(d % k for d in diffs):
            return -1
        return sum(filter(lambda x: x > 0, diffs)) // k



assert Solution().minOperations([4,3,1,4], [1,3,7,1], 3) == 2
assert Solution().minOperations([3,8,5,2], [2,4,1,6], 1) == -1
