# https://leetcode.com/problems/binary-tree-preorder-traversal
# easy
# practice - missed daily
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output, to_go = [], [root]
        while to_go:
            next_node = to_go.pop()
            if next_node is None:
                continue
            output.append(next_node.val)
            to_go.append(next_node.right)
            to_go.append(next_node.left)
        return output
