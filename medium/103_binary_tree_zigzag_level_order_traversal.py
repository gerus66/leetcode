# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal
# medium
# daily
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        to_go, ans = ([root], [[]]) if root else ([], [])
        next_to_go, rev = [], True
        while to_go:
            node = to_go.pop()
            ans[-1].append(node.val)
            children = [node.left, node.right] if rev else [node.right, node.left]
            next_to_go += [ch for ch in children if ch]
            if not to_go:
                to_go, next_to_go, rev = next_to_go, [], not rev
                ans.append([])
        return ans[:-1]
