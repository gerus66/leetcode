# https://leetcode.com/problems/shuffle-the-array
# easy
# daily
from typing import List
from itertools import chain


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return list(chain(*zip(nums[:n], nums[n:])))
