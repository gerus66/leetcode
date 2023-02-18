# https://leetcode.com/problems/invert-binary-tree
# easy
# daily
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        to_go = [root] if root else []
        while to_go:
            node = to_go.pop()
            node.left, node.right = node.right, node.left
            to_go.extend(x for x in [node.left, node.right] if x)
        return root
