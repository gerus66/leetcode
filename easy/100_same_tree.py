# https://leetcode.com/problems/same-tree
# easy
# practice - missed daily
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        to_go = [(p, q)]
        while to_go:
            (next_p, next_q) = to_go.pop()
            if next_p is None and next_q is None:
                continue
            if next_p is None or next_q is None:
                return False
            if next_p.val != next_q.val:
                return False
            to_go.append((next_p.right, next_q.right))
            to_go.append((next_p.left, next_q.left))
        return True
