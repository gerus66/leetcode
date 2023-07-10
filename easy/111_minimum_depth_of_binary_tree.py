# https://leetcode.com/problems/minimum-depth-of-binary-tree
# easy
# daily
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 1)])
        while q:
            node, depth = q.pop()
            if node is None:
                continue
            if node.left is None and node.right is None:
                return depth
            q.extendleft([(node.left, depth + 1), (node.right, depth + 1)])
        return 0
