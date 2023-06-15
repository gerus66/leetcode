# https://leetcode.com/problems/find-the-score-of-all-prefixes-of-an-array
# medium
# biweekly 102 - virtual
from typing import List


class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        ans = [nums[0]*2]
        prev_max = nums[0]
        for x in nums[1:]:
            ans.append(ans[-1] + (x*2 if x > prev_max else prev_max+x))
            prev_max = x if x > prev_max else prev_max
        return ans
