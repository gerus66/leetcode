# https://leetcode.com/problems/minimum-distance-between-bst-nodes
# easy
# daily
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        seen, to_go, diff, prev = set(), [root], 10**5, root.val
        while to_go:
            node = to_go.pop()
            if node.val not in seen:
                to_go.extend([node.right] if node.right else [])
                to_go.extend([node, node.left] if node.left else [])
            if (node.val in seen or node.left is None) and prev != node.val:
                diff, prev = min(diff, abs(prev-node.val)), node.val
            seen.add(node.val)
        return diff
