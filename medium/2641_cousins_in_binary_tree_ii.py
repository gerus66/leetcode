# https://leetcode.com/problems/cousins-in-binary-tree-ii
# medium
# biweekly 102 - virtual
from typing import Optional
import itertools


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        sums_by_level = []
        to_go = [root]
        while any(to_go):
            sums_by_level.append(sum(x.val for x in to_go if x))
            to_go = list(itertools.chain.from_iterable([x.left, x.right] for x in to_go if x))
        # print(sums_by_level)
        root.val = 0
        to_go, next_to_go, level = [root], [], 0
        while to_go:
            for node in to_go:
                if node is None or node.left is None and node.right is None:
                    continue
                cur_sum = (node.left.val if node.left else 0) + (node.right.val if node.right else 0)
                cur_val = sums_by_level[level + 1] - cur_sum
                if node.left:
                    node.left.val = cur_val
                if node.right:
                    node.right.val = cur_val
                next_to_go.extend([node.left, node.right])
            to_go, next_to_go, level = next_to_go, [], level + 1
        return root
