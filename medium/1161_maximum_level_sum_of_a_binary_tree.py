# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree
# medium
# daily
import itertools
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, level = -math.inf, 0
        cur_level, to_go = 0, [root]
        while any(to_go):
            cur_sum, cur_level = sum(x.val for x in to_go if x), cur_level + 1
            if cur_sum > max_sum:
                max_sum, level = cur_sum, cur_level
            to_go = list(itertools.chain.from_iterable([[x.left, x.right] for x in to_go if x]))
        return level
