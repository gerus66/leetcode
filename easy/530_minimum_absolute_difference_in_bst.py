# https://leetcode.com/problems/minimum-absolute-difference-in-bst
# easy
# daily
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        min_diff, prev = math.inf, None
        to_go, end = [root], False
        while to_go:
            if (cur:=to_go.pop()) is None:
                end = True
            else:
                if end:
                    if prev is None:
                        prev = cur.val
                    else:
                        min_diff, prev = min(min_diff, cur.val-prev), cur.val
                    end = False
                else:
                    to_go.extend([cur.right, cur, cur.left])
        return min_diff
