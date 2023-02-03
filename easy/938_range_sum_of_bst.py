# https://leetcode.com/problems/range-sum-of-bst
# easy
# practice - missed daily
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res, to_go = 0, [root]
        while to_go:
            node = to_go.pop()
            if node is not None:
                if low <= node.val <= high:
                    res += node.val
                    to_go.extend([node.left, node.right])
                elif node.val < low:
                    to_go.append(node.right)
                elif node.val > high:
                    to_go.append(node.left)
        return res
