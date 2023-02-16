# https://leetcode.com/problems/maximum-depth-of-binary-tree
# easy
# daily
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        h, to_go, next_to_go = 0, [root] if root else [], []
        while to_go:
            node = to_go.pop()
            next_to_go.extend(n for n in [node.left, node.right] if n is not None)
            if not to_go:
                h, to_go, next_to_go = h+1, next_to_go, []
        return h
