# https://leetcode.com/problems/leaf-similar-trees
# easy
# practice - missed daily
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def iter_by_leafs(tree):
        to_go = [tree]
        while to_go:
            node = to_go.pop()
            if node.right is None and node.left is None:
                yield node.val
            else:
                for child in [node.right, node.left]:
                    if child is not None:
                        to_go.append(child)
        yield None

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        for l1, l2 in zip(self.iter_by_leafs(root1), self.iter_by_leafs(root2)):
            if l1 != l2:
                return False
            if l1 is None:
                return True
